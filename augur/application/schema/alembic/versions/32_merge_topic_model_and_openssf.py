"""Merge: Add topic model meta table, update OpenSSF deps unique constraint

Revision ID: 32
Revises: 31
Create Date: 2025-07-xx

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '32'
down_revision = '31'
branch_labels = None
depends_on = None

def upgrade():
    # --- From 32_add_topic_model_meta_table.py ---
    op.create_table(
        'topic_model_meta',
        sa.Column('model_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('model_method', sa.Text(), nullable=False),
        sa.Column('num_topics', sa.Integer(), nullable=False),
        sa.Column('num_words_per_topic', sa.Integer(), nullable=False),
        sa.Column('training_parameters', postgresql.JSONB(), nullable=False),
        sa.Column('model_file_paths', postgresql.JSONB(), nullable=False),
        sa.Column('coherence_score', sa.Float(), nullable=True),
        sa.Column('perplexity_score', sa.Float(), nullable=True),
        sa.Column('training_start_time', sa.TIMESTAMP(), nullable=False),
        sa.Column('training_end_time', sa.TIMESTAMP(), nullable=False),
        sa.Column('tool_source', sa.Text(), nullable=False),
        sa.Column('tool_version', sa.Text(), nullable=False),
        sa.Column('data_source', sa.Text(), nullable=False),
        sa.Column('data_collection_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('model_id'),
        schema='augur_data'
    )
    op.add_column('repo_topic', sa.Column('model_id', postgresql.UUID(as_uuid=True), nullable=True), schema='augur_data')
    op.add_column('topic_words', sa.Column('model_id', postgresql.UUID(as_uuid=True), nullable=True), schema='augur_data')
    op.create_foreign_key(
        'fk_repo_topic_model_id',
        'repo_topic', 'topic_model_meta',
        ['model_id'], ['model_id'],
        source_schema='augur_data', referent_schema='augur_data',
        ondelete='SET NULL', onupdate='CASCADE'
    )
    op.create_foreign_key(
        'fk_topic_words_model_id',
        'topic_words', 'topic_model_meta',
        ['model_id'], ['model_id'],
        source_schema='augur_data', referent_schema='augur_data',
        ondelete='SET NULL', onupdate='CASCADE'
    )
    op.create_index('idx_repo_topic_model_id', 'repo_topic', ['model_id'], schema='augur_data')
    op.create_index('idx_topic_words_model_id', 'topic_words', ['model_id'], schema='augur_data')

    # --- From 32_update_openssf_deps.py ---
    op.drop_constraint(
        'deps-scorecard-insert-unique',
        'repo_deps_scorecard',
        schema='augur_data',
        type_='unique'
    )
    op.create_unique_constraint(
        'deps_scorecard_new_unique',
        'repo_deps_scorecard',
        ['repo_id', 'repo_deps_scorecard_id'],
        schema='augur_data'
    )

def downgrade():
    # --- From 32_update_openssf_deps.py ---
    op.drop_constraint(
        'deps_scorecard_new_unique',
        'repo_deps_scorecard',
        schema='augur_data',
        type_='unique'
    )
    op.create_unique_constraint(
        'deps-scorecard-insert-unique',
        'repo_deps_scorecard',
        ['repo_id', 'name'],
        schema='augur_data'
    )

    # --- From 32_add_topic_model_meta_table.py ---
    op.drop_index('idx_topic_words_model_id', table_name='topic_words', schema='augur_data')
    op.drop_index('idx_repo_topic_model_id', table_name='repo_topic', schema='augur_data')
    op.drop_constraint('fk_topic_words_model_id', 'topic_words', schema='augur_data', type_='foreignkey')
    op.drop_constraint('fk_repo_topic_model_id', 'repo_topic', schema='augur_data', type_='foreignkey')
    op.drop_column('topic_words', 'model_id', schema='augur_data')
    op.drop_column('repo_topic', 'model_id', schema='augur_data')
    op.drop_table('topic_model_meta', schema='augur_data') 