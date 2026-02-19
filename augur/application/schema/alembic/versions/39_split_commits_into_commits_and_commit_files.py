"""Split commits into commits and commit_files tables

Revision ID: 39
Revises: 38
Create Date: 2026-02-19 17:30:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '39'
down_revision = '38'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    # Step 0: Dynamically backup and drop ALL materialized views BEFORE any schema changes.
    # By doing this BEFORE renaming the commits table, pg_get_viewdef correctly captures their original
    # dependencies on 'commits' and 'cmt_id', instead of automatically tracking renaming to 'commit_files'.
    op.execute(sa.text('''
        CREATE TABLE IF NOT EXISTS augur_data.temp_backed_up_mviews (
            view_name text PRIMARY KEY,
            view_definition text
        );
    '''))
    
    op.execute(sa.text("TRUNCATE augur_data.temp_backed_up_mviews;"))

    res = bind.execute(sa.text("SELECT matviewname FROM pg_matviews WHERE schemaname = 'augur_data'"))
    all_mviews = [r[0] for r in res]
    
    for mv in all_mviews:
        try:
            def_res = bind.execute(sa.text("SELECT pg_get_viewdef('augur_data.' || :mv, true)"), {'mv': mv}).scalar()
            if def_res:
                bind.execute(
                    sa.text("INSERT INTO augur_data.temp_backed_up_mviews (view_name, view_definition) VALUES (:name, :def) ON CONFLICT DO NOTHING"),
                    {'name': mv, 'def': def_res}
                )
        except Exception as e:
            pass

    for mv in all_mviews:
        op.execute(sa.text(f"DROP MATERIALIZED VIEW IF EXISTS augur_data.{mv} CASCADE;"))

    # Step 1: Rename the existing "commits" table to "commit_files"
    op.rename_table('commits', 'commit_files', schema='augur_data')

    # Step 1b: Rename the old sequence too, to avoid collision when we create the new table. 
    # It's currently attached to the renamed table.
    op.execute(sa.text("""
        ALTER SEQUENCE IF EXISTS augur_data.commits_cmt_id_seq 
        RENAME TO commit_files_commit_file_id_seq;
    """))

    # Step 2: Create new "commits" table with commit-level columns only.
    # Introspect column types from the renamed commit_files table to ensure
    # correct types (e.g. cmt_ght_author_id may be BigInteger or UUID depending
    # on the contributors.cntrb_id type in this database).
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing_cols = {c['name']: c for c in inspector.get_columns('commit_files', schema='augur_data')}

    def _col_type(name):
        """Get the actual column type from the existing commit_files table."""
        return existing_cols[name]['type']

    op.create_table('commits',
        sa.Column('cmt_id', sa.BigInteger, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('repo_id', _col_type('repo_id'), nullable=False),
        sa.Column('cmt_commit_hash', _col_type('cmt_commit_hash'), nullable=False),
        sa.Column('cmt_author_name', _col_type('cmt_author_name'), nullable=False),
        sa.Column('cmt_author_raw_email', _col_type('cmt_author_raw_email'), nullable=False),
        sa.Column('cmt_author_email', _col_type('cmt_author_email'), nullable=False),
        sa.Column('cmt_author_date', _col_type('cmt_author_date'), nullable=False),
        sa.Column('cmt_author_affiliation', _col_type('cmt_author_affiliation'),
                  server_default=sa.text("'NULL'::character varying"), nullable=True),
        sa.Column('cmt_committer_name', _col_type('cmt_committer_name'), nullable=False),
        sa.Column('cmt_committer_raw_email', _col_type('cmt_committer_raw_email'), nullable=False),
        sa.Column('cmt_committer_email', _col_type('cmt_committer_email'), nullable=False),
        sa.Column('cmt_committer_date', _col_type('cmt_committer_date'), nullable=False),
        sa.Column('cmt_committer_affiliation', _col_type('cmt_committer_affiliation'),
                  server_default=sa.text("'NULL'::character varying"), nullable=True),
        sa.Column('cmt_date_attempted', _col_type('cmt_date_attempted'), nullable=False),
        sa.Column('cmt_ght_author_id', _col_type('cmt_ght_author_id'), nullable=True),
        sa.Column('cmt_ght_committer_id', _col_type('cmt_ght_committer_id'), nullable=True),
        sa.Column('cmt_ght_committed_at', _col_type('cmt_ght_committed_at'), nullable=True),
        sa.Column('cmt_committer_timestamp', _col_type('cmt_committer_timestamp'), nullable=True),
        sa.Column('cmt_author_timestamp', _col_type('cmt_author_timestamp'), nullable=True),
        sa.Column('cmt_author_platform_username', _col_type('cmt_author_platform_username'), nullable=True),
        sa.Column('tool_source', _col_type('tool_source'), nullable=True),
        sa.Column('tool_version', _col_type('tool_version'), nullable=True),
        sa.Column('data_source', _col_type('data_source'), nullable=True),
        sa.Column('data_collection_date', _col_type('data_collection_date'),
                  server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.ForeignKeyConstraint(['repo_id'], ['augur_data.repo.repo_id'],
                                onupdate='CASCADE', ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('cmt_id'),
        sa.UniqueConstraint('repo_id', 'cmt_commit_hash', name='commits_repo_id_cmt_commit_hash_unique'),
        schema='augur_data',
        comment='Commits. Each row represents a single commit. '
                'File-level details are stored in the commit_files table.'
    )

    # Recreate FK constraints to contributors that existed on the original commits table.
    # We introspect the renamed commit_files table to discover which FKs actually exist,
    # because not all databases have the same constraints (e.g. cntrb_login may lack
    # a unique constraint, making fk_commits_contributors_3 impossible).
    existing_fks = inspector.get_foreign_keys('commit_files', schema='augur_data')
    for fk in existing_fks:
        ref_table = fk['referred_table']
        ref_schema = fk.get('referred_schema', 'augur_data')
        # Only recreate FKs pointing to contributors (repo FK is already in create_table)
        if ref_table != 'contributors':
            continue
        fk_name = fk.get('name')
        local_cols = fk['constrained_columns']
        remote_cols = fk['referred_columns']
        fk_options = fk.get('options', {})
        op.create_foreign_key(
            fk_name, 'commits', ref_table,
            local_cols, remote_cols,
            source_schema='augur_data', referent_schema=ref_schema,
            onupdate=fk_options.get('onupdate'),
            ondelete=fk_options.get('ondelete'),
            initially=fk_options.get('initially'),
            deferrable=fk_options.get('deferrable'),
        )


    # Step 2b: Create new distinct indexes for the commits table
    op.create_index('commits_author_affiliation_idx', 'commits', ['cmt_author_affiliation'], schema='augur_data')
    op.create_index('commits_author_cntrb_id_idx', 'commits', ['cmt_ght_author_id'], schema='augur_data')
    op.create_index('commits_author_raw_email_idx', 'commits', ['cmt_author_raw_email'], schema='augur_data')
    op.create_index('commits_commited_idx', 'commits', ['cmt_id'], schema='augur_data')
    op.create_index('commits_author_email_date_name_idx', 'commits',
                     ['cmt_author_email', 'cmt_author_date', 'cmt_author_name'], schema='augur_data')
    op.create_index('commits_committer_affiliation_idx', 'commits', ['cmt_committer_affiliation'],
                     schema='augur_data', postgresql_using='hash')
    op.create_index('commits_author_email_affiliation_date_idx', 'commits',
                     ['cmt_author_email', 'cmt_author_affiliation', 'cmt_author_date'], schema='augur_data')
    op.create_index('commits_committer_raw_email_idx', 'commits', ['cmt_committer_raw_email'], schema='augur_data')
    op.create_index('commits_repo_id_commit_hash_idx', 'commits', ['repo_id', 'cmt_commit_hash'], schema='augur_data')

    # Step 3: Backfill the new commits table with deduplicated data from commit_files
    # Uses DISTINCT ON to pick one representative row per (repo_id, cmt_commit_hash)
    # The cmt_id will just automatically map to the new SERIAL sequence cleanly.
    op.execute(sa.text("""
        INSERT INTO augur_data.commits (
            repo_id, cmt_commit_hash,
            cmt_author_name, cmt_author_raw_email, cmt_author_email, cmt_author_date,
            cmt_author_affiliation,
            cmt_committer_name, cmt_committer_raw_email, cmt_committer_email, cmt_committer_date,
            cmt_committer_affiliation,
            cmt_date_attempted, cmt_ght_author_id, cmt_ght_committer_id, cmt_ght_committed_at,
            cmt_committer_timestamp, cmt_author_timestamp, cmt_author_platform_username,
            tool_source, tool_version, data_source, data_collection_date
        )
        SELECT DISTINCT ON (repo_id, cmt_commit_hash)
            repo_id, cmt_commit_hash,
            cmt_author_name, cmt_author_raw_email, cmt_author_email, cmt_author_date,
            cmt_author_affiliation,
            cmt_committer_name, cmt_committer_raw_email, cmt_committer_email, cmt_committer_date,
            cmt_committer_affiliation,
            cmt_date_attempted, cmt_ght_author_id, cmt_ght_committer_id, cmt_ght_committed_at,
            cmt_committer_timestamp, cmt_author_timestamp, cmt_author_platform_username,
            tool_source, tool_version, data_source, data_collection_date
        FROM augur_data.commit_files
        ORDER BY repo_id, cmt_commit_hash, cmt_id
    """))

    # Step 4: Add commit_id FK column to commit_files and a new PK column
    op.add_column('commit_files',
                  sa.Column('commit_id', _col_type('cmt_id'), nullable=True),
                  schema='augur_data')

    # Step 5: Populate commit_id FK in commit_files
    op.execute(sa.text("""
        UPDATE augur_data.commit_files cf
        SET commit_id = c.cmt_id
        FROM augur_data.commits c
        WHERE cf.repo_id = c.repo_id
          AND cf.cmt_commit_hash = c.cmt_commit_hash
    """))

    # Step 6: Make commit_id NOT NULL now that it's populated
    op.alter_column('commit_files', 'commit_id', nullable=False, schema='augur_data')

    # Step 7: Add FK constraint from commit_files.commit_id -> commits.cmt_id
    op.create_foreign_key(
        'fk_commit_files_commits',
        'commit_files', 'commits',
        ['commit_id'], ['cmt_id'],
        source_schema='augur_data', referent_schema='augur_data',
        ondelete='CASCADE', onupdate='CASCADE'
    )

    # Step 8: Rename old PK cmt_id to commit_file_id
    op.alter_column('commit_files', 'cmt_id', new_column_name='commit_file_id', schema='augur_data')

    # Step 9: Remap FK references in commit_parents and commit_comment_ref
    # IMPORTANT: This must happen BEFORE dropping columns from commit_files,
    # because the old cmt_id values in these tables correspond to commit_files.commit_file_id.
    # We use commit_files.commit_id (populated in Step 5) to map to the new commits.cmt_id.
    #
    # FK names are introspected dynamically because they vary across databases
    # (e.g. the base schema uses fk_commit_parents_commits_1/2, but auto-generated
    # names could differ).

    # Introspect and drop FKs on commit_parents that reference commit_files
    # (commit_files was originally 'commits', so FKs pointing to commits.cmt_id
    # now reference commit_files.cmt_id after the rename, but cmt_id was renamed
    # to commit_file_id in Step 8).
    cp_fks = inspector.get_foreign_keys('commit_parents', schema='augur_data')
    cp_fk_names = []
    for fk in cp_fks:
        # After rename, FKs that pointed to commits now point to commit_files
        if fk['referred_table'] in ('commits', 'commit_files'):
            fk_name = fk['name']
            cp_fk_names.append({
                'name': fk_name,
                'constrained_columns': fk['constrained_columns'],
                'referred_columns': fk['referred_columns'],
                'options': fk.get('options', {}),
            })
            op.drop_constraint(fk_name, 'commit_parents', type_='foreignkey', schema='augur_data')

    # Remap commit_parents.cmt_id: old per-file ID -> new per-commit ID
    # commit_files.commit_file_id is the old cmt_id, commit_files.commit_id is the new commits.cmt_id
    op.execute(sa.text("""
        UPDATE augur_data.commit_parents AS cp
        SET cmt_id = cf.commit_id
        FROM augur_data.commit_files AS cf
        WHERE cf.commit_file_id = cp.cmt_id
    """))

    # Remap commit_parents.parent_id similarly
    op.execute(sa.text("""
        UPDATE augur_data.commit_parents AS cp
        SET parent_id = cf.commit_id
        FROM augur_data.commit_files AS cf
        WHERE cf.commit_file_id = cp.parent_id
    """))

    # Recreate FK constraints on commit_parents pointing to new commits table
    for fk_info in cp_fk_names:
        op.create_foreign_key(
            fk_info['name'], 'commit_parents', 'commits',
            fk_info['constrained_columns'], ['cmt_id'],
            source_schema='augur_data', referent_schema='augur_data',
            onupdate=fk_info['options'].get('onupdate'),
            ondelete=fk_info['options'].get('ondelete'),
        )

    # Remap commit_comment_ref FK — introspect the actual FK name
    ccr_fks = inspector.get_foreign_keys('commit_comment_ref', schema='augur_data')
    ccr_fk_info = None
    for fk in ccr_fks:
        if fk['referred_table'] in ('commits', 'commit_files') and 'cmt_id' in fk['constrained_columns']:
            ccr_fk_info = {
                'name': fk['name'],
                'options': fk.get('options', {}),
            }
            op.drop_constraint(fk['name'], 'commit_comment_ref', type_='foreignkey', schema='augur_data')
            break

    op.execute(sa.text("""
        UPDATE augur_data.commit_comment_ref AS ccr
        SET cmt_id = cf.commit_id
        FROM augur_data.commit_files AS cf
        WHERE cf.commit_file_id = ccr.cmt_id
    """))

    ccr_fk_name = ccr_fk_info['name'] if ccr_fk_info else 'fk_commit_comment_ref_commits_1'
    ccr_options = ccr_fk_info['options'] if ccr_fk_info else {}
    op.create_foreign_key(
        ccr_fk_name, 'commit_comment_ref', 'commits',
        ['cmt_id'], ['cmt_id'],
        source_schema='augur_data', referent_schema='augur_data',
        ondelete=ccr_options.get('ondelete', 'RESTRICT'),
        onupdate=ccr_options.get('onupdate', 'CASCADE'),
    )




    # Step 10: Now safe to drop redundant commit-level columns from commit_files
    columns_to_drop = [
        'cmt_commit_hash',
        'cmt_author_name', 'cmt_author_raw_email', 'cmt_author_email', 'cmt_author_date',
        'cmt_author_affiliation',
        'cmt_committer_name', 'cmt_committer_raw_email', 'cmt_committer_email', 'cmt_committer_date',
        'cmt_committer_affiliation',
        'cmt_date_attempted',
        'cmt_ght_author_id', 'cmt_ght_committer_id', 'cmt_ght_committed_at',
        'cmt_committer_timestamp', 'cmt_author_timestamp',
        'cmt_author_platform_username',
    ]
    for col in columns_to_drop:
        op.drop_column('commit_files', col, schema='augur_data')

    # Step 11: Add indexes on commit_files
    op.create_index('commit_files_commit_id_idx', 'commit_files', ['commit_id'], schema='augur_data')
    op.create_index('commit_files_repo_id_idx', 'commit_files', ['repo_id'], schema='augur_data')

    # Step 12: Add unique constraint on commit_files (commit_id, cmt_filename)
    op.create_unique_constraint(
        'commit_files_commit_id_cmt_filename_unique',
        'commit_files', ['commit_id', 'cmt_filename'],
        schema='augur_data'
    )

    # Step 13: Update table comment and ensure sequence is correctly linked
    op.execute(sa.text("""
        COMMENT ON TABLE augur_data.commit_files IS
        'Commit file-level data. Each row represents changes to one file within a single commit, linked to the commits table.'
    """))

    # Step 13b: Drop all redundant legacy indexes from commit_files dynamically, ensuring avoiding collisions with arbitrary old DB states.
    cf_indexes = inspector.get_indexes('commit_files', schema='augur_data')
    # the indexes we just safely created on commit_files that must be kept
    indexes_to_keep = {
        'commit_files_commit_id_idx', 
        'commit_files_repo_id_idx', 
        'commit_files_commit_id_cmt_filename_unique'
    }
    
    for idx in cf_indexes:
        idx_name = idx['name']
        if idx_name not in indexes_to_keep:
            op.execute(sa.text(f'DROP INDEX IF EXISTS augur_data."{idx_name}" CASCADE'))



    # Step 14: Recreate Materialized Views dynamically from backup
    bind = op.get_bind()
    res = bind.execute(sa.text("SELECT view_name, view_definition FROM augur_data.temp_backed_up_mviews"))
    
    for r in res:
        mv_name = r[0]
        mv_def = r[1]
        
        # Since we backed up the definitions BEFORE commits was renamed, they all natively expect
        # columns from the original 'commits' table, which now perfectly maps to the new 'commits'
        # table schema for 99% of views. However, if a view uses file-level columns (cmt_added, cmt_removed),
        # those moved to 'commit_files', so we must manually override their queries.
        
        if mv_name == 'explorer_pr_response_times':
             mv_def = """
SELECT repo.repo_id,
    pull_requests.pr_src_id,
    repo.repo_name,
    pull_requests.pr_src_author_association,
    repo_groups.rg_name AS repo_group,
    pull_requests.pr_src_state,
    pull_requests.pr_merged_at,
    pull_requests.pr_created_at,
    pull_requests.pr_closed_at,
    date_part('year'::text, pull_requests.pr_created_at::date) AS created_year,
    date_part('month'::text, pull_requests.pr_created_at::date) AS created_month,
    date_part('year'::text, pull_requests.pr_closed_at::date) AS closed_year,
    date_part('month'::text, pull_requests.pr_closed_at::date) AS closed_month,
    base_labels.pr_src_meta_label,
    base_labels.pr_head_or_base,
    (EXTRACT(epoch FROM pull_requests.pr_closed_at) - EXTRACT(epoch FROM pull_requests.pr_created_at)) / 3600::numeric AS hours_to_close,
    (EXTRACT(epoch FROM pull_requests.pr_closed_at) - EXTRACT(epoch FROM pull_requests.pr_created_at)) / 86400::numeric AS days_to_close,
    (EXTRACT(epoch FROM response_times.first_response_time) - EXTRACT(epoch FROM pull_requests.pr_created_at)) / 3600::numeric AS hours_to_first_response,
    (EXTRACT(epoch FROM response_times.first_response_time) - EXTRACT(epoch FROM pull_requests.pr_created_at)) / 86400::numeric AS days_to_first_response,
    (EXTRACT(epoch FROM response_times.last_response_time) - EXTRACT(epoch FROM pull_requests.pr_created_at)) / 3600::numeric AS hours_to_last_response,
    (EXTRACT(epoch FROM response_times.last_response_time) - EXTRACT(epoch FROM pull_requests.pr_created_at)) / 86400::numeric AS days_to_last_response,
    response_times.first_response_time,
    response_times.last_response_time,
    response_times.average_time_between_responses,
    response_times.assigned_count,
    response_times.review_requested_count,
    response_times.labeled_count,
    response_times.subscribed_count,
    response_times.mentioned_count,
    response_times.referenced_count,
    response_times.closed_count,
    response_times.head_ref_force_pushed_count,
    response_times.merged_count,
    response_times.milestoned_count,
    response_times.unlabeled_count,
    response_times.head_ref_deleted_count,
    response_times.comment_count,
    master_merged_counts.lines_added,
    master_merged_counts.lines_removed,
    all_commit_counts.commit_count,
    master_merged_counts.file_count
   FROM augur_data.repo,
    augur_data.repo_groups,
    augur_data.pull_requests
     LEFT JOIN ( SELECT pull_requests_1.pull_request_id,
            count(*) FILTER (WHERE pull_request_events.action::text = 'assigned'::text) AS assigned_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'review_requested'::text) AS review_requested_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'labeled'::text) AS labeled_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'unlabeled'::text) AS unlabeled_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'subscribed'::text) AS subscribed_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'mentioned'::text) AS mentioned_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'referenced'::text) AS referenced_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'closed'::text) AS closed_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'head_ref_force_pushed'::text) AS head_ref_force_pushed_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'head_ref_deleted'::text) AS head_ref_deleted_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'milestoned'::text) AS milestoned_count,
            count(*) FILTER (WHERE pull_request_events.action::text = 'merged'::text) AS merged_count,
            min(message.msg_timestamp) AS first_response_time,
            count(DISTINCT message.msg_timestamp) AS comment_count,
            max(message.msg_timestamp) AS last_response_time,
            (max(message.msg_timestamp) - min(message.msg_timestamp)) / count(DISTINCT message.msg_timestamp)::double precision AS average_time_between_responses
           FROM augur_data.pull_request_events,
            augur_data.pull_requests pull_requests_1,
            augur_data.repo repo_1,
            augur_data.pull_request_message_ref,
            augur_data.message
          WHERE repo_1.repo_id = pull_requests_1.repo_id AND pull_requests_1.pull_request_id = pull_request_events.pull_request_id AND pull_requests_1.pull_request_id = pull_request_message_ref.pull_request_id AND pull_request_message_ref.msg_id = message.msg_id
          GROUP BY pull_requests_1.pull_request_id) response_times ON pull_requests.pull_request_id = response_times.pull_request_id
     LEFT JOIN ( SELECT pull_request_commits.pull_request_id,
            count(DISTINCT pull_request_commits.pr_cmt_sha) AS commit_count
           FROM augur_data.pull_request_commits,
            augur_data.pull_requests pull_requests_1,
            augur_data.pull_request_meta
          WHERE pull_requests_1.pull_request_id = pull_request_commits.pull_request_id AND pull_requests_1.pull_request_id = pull_request_meta.pull_request_id AND pull_request_commits.pr_cmt_sha::text <> pull_requests_1.pr_merge_commit_sha::text AND pull_request_commits.pr_cmt_sha::text <> pull_request_meta.pr_sha::text
          GROUP BY pull_request_commits.pull_request_id) all_commit_counts ON pull_requests.pull_request_id = all_commit_counts.pull_request_id
     LEFT JOIN ( SELECT max(pull_request_meta.pr_repo_meta_id) AS max,
            pull_request_meta.pull_request_id,
            pull_request_meta.pr_head_or_base,
            pull_request_meta.pr_src_meta_label
           FROM augur_data.pull_requests pull_requests_1,
            augur_data.pull_request_meta
          WHERE pull_requests_1.pull_request_id = pull_request_meta.pull_request_id AND pull_request_meta.pr_head_or_base::text = 'base'::text
          GROUP BY pull_request_meta.pull_request_id, pull_request_meta.pr_head_or_base, pull_request_meta.pr_src_meta_label) base_labels ON base_labels.pull_request_id = all_commit_counts.pull_request_id
     LEFT JOIN ( SELECT sum(commit_files.cmt_added) AS lines_added,
            sum(commit_files.cmt_removed) AS lines_removed,
            pull_request_commits.pull_request_id,
            count(DISTINCT commit_files.cmt_filename) AS file_count
           FROM augur_data.pull_request_commits,
            augur_data.commits,
            augur_data.commit_files,
            augur_data.pull_requests pull_requests_1,
            augur_data.pull_request_meta
          WHERE ((commits.cmt_id = commit_files.commit_id) AND (commits.cmt_commit_hash::text = pull_request_commits.pr_cmt_sha::text) AND (pull_requests_1.pull_request_id = pull_request_commits.pull_request_id) AND (pull_requests_1.pull_request_id = pull_request_meta.pull_request_id) AND (commits.repo_id = pull_requests_1.repo_id) AND (commits.cmt_commit_hash::text <> pull_requests_1.pr_merge_commit_sha::text) AND (commits.cmt_commit_hash::text <> pull_request_meta.pr_sha::text))
          GROUP BY pull_request_commits.pull_request_id) master_merged_counts ON base_labels.pull_request_id = master_merged_counts.pull_request_id
  WHERE repo.repo_group_id = repo_groups.repo_group_id AND repo.repo_id = pull_requests.repo_id
  ORDER BY response_times.merged_count DESC
"""
        
        try:
            op.execute(sa.text(f"CREATE MATERIALIZED VIEW augur_data.{mv_name} AS {mv_def}"))
        except Exception as e:
            pass

    # Restore unique indexes if needed
    op.execute(sa.text("CREATE UNIQUE INDEX IF NOT EXISTS explorer_pr_response_times_idx ON augur_data.explorer_pr_response_times(repo_id, pr_src_id, pr_src_meta_label);"))
    op.execute(sa.text("DROP TABLE IF EXISTS augur_data.temp_backed_up_mviews;"))


def downgrade():
    # Drop Materialized Views before modifying schemas
    bind = op.get_bind()
    res = bind.execute(sa.text("SELECT matviewname FROM pg_matviews WHERE schemaname = 'augur_data'"))
    all_mviews = [r[0] for r in res]
    for mv in all_mviews:
        op.execute(sa.text(f"DROP MATERIALIZED VIEW IF EXISTS augur_data.{mv} CASCADE;"))

    # This is a complex migration. The downgrade merges commit_files back into commits.

    # Drop the new commits table and rename commit_files back to commits
    # First, re-add the commit-level columns to commit_files
    # Introspect column types from the commits table to re-add them correctly.
    # This avoids type mismatches (e.g. cmt_ght_author_id may be UUID, not BigInteger).
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    commits_cols = {c['name']: c for c in inspector.get_columns('commits', schema='augur_data')}

    columns_to_restore = [
        'cmt_commit_hash', 'cmt_author_name', 'cmt_author_raw_email',
        'cmt_author_email', 'cmt_author_date', 'cmt_author_affiliation',
        'cmt_committer_name', 'cmt_committer_raw_email', 'cmt_committer_email',
        'cmt_committer_date', 'cmt_committer_affiliation', 'cmt_date_attempted',
        'cmt_ght_author_id', 'cmt_ght_committer_id', 'cmt_ght_committed_at',
        'cmt_committer_timestamp', 'cmt_author_timestamp',
        'cmt_author_platform_username',
    ]
    for col_name in columns_to_restore:
        col_info = commits_cols[col_name]
        op.add_column('commit_files',
                      sa.Column(col_name, col_info['type'], nullable=True),
                      schema='augur_data')


    # Populate commit-level columns from the commits table
    op.execute(sa.text("""
        UPDATE augur_data.commit_files cf SET
            cmt_commit_hash = c.cmt_commit_hash,
            cmt_author_name = c.cmt_author_name,
            cmt_author_raw_email = c.cmt_author_raw_email,
            cmt_author_email = c.cmt_author_email,
            cmt_author_date = c.cmt_author_date,
            cmt_author_affiliation = c.cmt_author_affiliation,
            cmt_committer_name = c.cmt_committer_name,
            cmt_committer_raw_email = c.cmt_committer_raw_email,
            cmt_committer_email = c.cmt_committer_email,
            cmt_committer_date = c.cmt_committer_date,
            cmt_committer_affiliation = c.cmt_committer_affiliation,
            cmt_date_attempted = c.cmt_date_attempted,
            cmt_ght_author_id = c.cmt_ght_author_id,
            cmt_ght_committer_id = c.cmt_ght_committer_id,
            cmt_ght_committed_at = c.cmt_ght_committed_at,
            cmt_committer_timestamp = c.cmt_committer_timestamp,
            cmt_author_timestamp = c.cmt_author_timestamp,
            cmt_author_platform_username = c.cmt_author_platform_username
        FROM augur_data.commits c
        WHERE cf.commit_id = c.cmt_id
    """))

    # Rename commit_file_id back to cmt_id
    op.alter_column('commit_files', 'commit_file_id', new_column_name='cmt_id', schema='augur_data')

    # Drop unique constraint BEFORE dropping commit_id (constraint references commit_id)
    op.drop_constraint('commit_files_commit_id_cmt_filename_unique', 'commit_files', type_='unique', schema='augur_data')

    # Drop indexes on commit_id BEFORE dropping the column
    op.drop_index('commit_files_commit_id_idx', 'commit_files', schema='augur_data')
    op.drop_index('commit_files_repo_id_idx', 'commit_files', schema='augur_data')

    # Drop commit_id column and FK
    op.drop_constraint('fk_commit_files_commits', 'commit_files', type_='foreignkey', schema='augur_data')
    op.drop_column('commit_files', 'commit_id', schema='augur_data')


    # Introspect and drop FK constraints on commit_parents and commit_comment_ref
    # that point to the new commits table (created during upgrade).
    # We preserve the FK names/options so we can recreate them after the rename.
    cp_fks = inspector.get_foreign_keys('commit_parents', schema='augur_data')
    cp_fk_infos = []
    for fk in cp_fks:
        if fk['referred_table'] == 'commits':
            cp_fk_infos.append({
                'name': fk['name'],
                'constrained_columns': fk['constrained_columns'],
                'options': fk.get('options', {}),
            })
            op.drop_constraint(fk['name'], 'commit_parents', type_='foreignkey', schema='augur_data')

    ccr_fks = inspector.get_foreign_keys('commit_comment_ref', schema='augur_data')
    ccr_fk_info = None
    for fk in ccr_fks:
        if fk['referred_table'] == 'commits' and 'cmt_id' in fk['constrained_columns']:
            ccr_fk_info = {
                'name': fk['name'],
                'options': fk.get('options', {}),
            }
            op.drop_constraint(fk['name'], 'commit_comment_ref', type_='foreignkey', schema='augur_data')
            break

    # Drop the new commits table
    op.drop_table('commits', schema='augur_data')

    # Rename commit_files back to commits
    op.rename_table('commit_files', 'commits', schema='augur_data')

    # Step 1b: Rename the sequence back
    op.execute(sa.text("""
        ALTER SEQUENCE IF EXISTS augur_data.commit_files_commit_file_id_seq 
        RENAME TO commits_cmt_id_seq;
    """))

    # Restore FK constraints on commit_parents pointing to the restored commits table
    for fk_info in cp_fk_infos:
        op.create_foreign_key(
            fk_info['name'], 'commit_parents', 'commits',
            fk_info['constrained_columns'], ['cmt_id'],
            source_schema='augur_data', referent_schema='augur_data',
            onupdate=fk_info['options'].get('onupdate'),
            ondelete=fk_info['options'].get('ondelete'),
        )

    # Restore FK constraint on commit_comment_ref
    if ccr_fk_info:
        op.create_foreign_key(
            ccr_fk_info['name'], 'commit_comment_ref', 'commits',
            ['cmt_id'], ['cmt_id'],
            source_schema='augur_data', referent_schema='augur_data',
            ondelete=ccr_fk_info['options'].get('ondelete', 'RESTRICT'),
            onupdate=ccr_fk_info['options'].get('onupdate', 'CASCADE'),
        )

    # Note: the new clean indexes (e.g. 'commits_author_affiliation_idx') we created on commits 
    # during upgrade were automatically dropped when we ran op.drop_table('commits').
    
    # Restore original indexes on the commits table that were moved
    op.create_index('author_affiliation', 'commits', ['cmt_author_affiliation'], schema='augur_data')
    op.create_index('author_cntrb_id', 'commits', ['cmt_ght_author_id'], schema='augur_data')
    op.create_index('author_raw_email', 'commits', ['cmt_author_raw_email'], schema='augur_data')
    op.create_index('commited', 'commits', ['cmt_id'], schema='augur_data')
    op.create_index('commits_idx_cmt_email_cmt_date_cmt_name', 'commits',
                     ['cmt_author_email', 'cmt_author_date', 'cmt_author_name'], schema='augur_data')
    op.create_index('committer_affiliation', 'commits', ['cmt_committer_affiliation'],
                     schema='augur_data', postgresql_using='hash')
    op.create_index('author_email,author_affiliation,author_date', 'commits',
                     ['cmt_author_email', 'cmt_author_affiliation', 'cmt_author_date'], schema='augur_data')
    op.create_index('committer_raw_email', 'commits', ['cmt_committer_raw_email'], schema='augur_data')
    op.create_index('repo_id,commit', 'commits', ['repo_id', 'cmt_commit_hash'], schema='augur_data')

    # Note: Downgrade restores the schema, so the user might need to rerun the old migrations to restore views perfectly, 
    # but since this is downgrade we can just leave the views dropped or try to restore from backup table if it exists
    bind = op.get_bind()
    try:
        res = bind.execute(sa.text("SELECT view_name, view_definition FROM augur_data.temp_backed_up_mviews"))
        for r in res:
            op.execute(sa.text(f"CREATE MATERIALIZED VIEW augur_data.{r[0]} AS {r[1]}"))
        op.execute(sa.text("DROP TABLE IF EXISTS augur_data.temp_backed_up_mviews;"))
    except:
        pass

