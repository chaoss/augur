from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('platform_features', sa.Column('worker_run_id', sa.BIGINT(), autoincrement=False, nullable=True, comment='This column is used to indicate analyses run by a worker during the same execution period, and is useful for grouping, and time series analysis.'))
    op.add_column('platform_features', sa.Column('dep_name', sa.VARCHAR(), autoincrement=False, nullable=True, comment='Name of the dependency found in project.'))
    op.add_column('platform_features', sa.Column('dep_count', sa.INTEGER(), autoincrement=False, nullable=True, comment='Number of times the dependency was found.'))
    op.add_column('platform_features', sa.Column('dep_language', sa.VARCHAR(), autoincrement=False, nullable=True, comment='Language of the dependency.'))
    op.add_column('platform_features', sa.Column('pull_request_info', sa.VARCHAR(), autoincrement=False, nullable=True, comment='This is a representation of the repo:branch information in the pull request. Head is issuing the pull request and base is taking the pull request. For example: (We do not store all of this)\n\n "head": {\n      "label": "chaoss:pull-request-worker",\n      "ref": "pull-request-worke'))

def downgrade():
    op.drop_column('platform_features', 'worker_run_id')
    op.drop_column('platform_features', 'dep_name')
    op.drop_column('platform_features', 'dep_count')
    op.drop_column('platform_features', 'dep_language')
    op.drop_column('platform_features', 'pull_request_info') 