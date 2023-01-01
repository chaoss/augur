"""traffic additions

Revision ID: 3
Revises: 2
Create Date: 2022-12-30 19:23:17.997570

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3'
down_revision = '2'
branch_labels = None
depends_on = None


def upgrade():

    add_repo_clone_data_table_1()

def downgrade():

    upgrade = False

    add_repo_clone_data_table_1(upgrade)
    

def add_repo_clone_data_table_1(upgrade = True):

    if upgrade:

        op.create_table('repo_clones_data',
        sa.Column('repo_clone_data_id', sa.BigInteger(), server_default=sa.text("nextval('augur_data.repo_clones_data_id_seq'::regclass)"), nullable=False),
        sa.Column('repo_id', sa.BigInteger(), nullable=False),
        sa.Column('unique_clones', sa.BigInteger(), nullable=True),
        sa.Column('count_clones', sa.BigInteger(), nullable=True),
        sa.Column('clone_data_timestamp', postgresql.TIMESTAMP(precision=6), nullable=True),
        sa.ForeignKeyConstraint(['repo_id'], ['augur_data.repo.repo_id'], onupdate='CASCADE', ondelete='RESTRICT', initially='DEFERRED', deferrable=True),
        sa.PrimaryKeyConstraint('repo_clone_data_id'),
        schema='augur_data'
        )
        op.alter_column('releases', 'release_id',
                existing_type=sa.CHAR(length=256),
                type_=sa.CHAR(length=128),
                existing_nullable=False,
                existing_server_default=sa.text('nextval(\'"augur_data".releases_release_id_seq\'::regclass)'),
                schema='augur_data')
        op.drop_constraint('user_repos_repo_id_fkey', 'user_repos', schema='augur_operations', type_='foreignkey')
        op.create_foreign_key(None, 'user_repos', 'repo', ['repo_id'], ['repo_id'], source_schema='augur_operations', referent_schema='augur_data')
    
    else:
        
        op.drop_constraint(None, 'user_repos', schema='augur_operations', type_='foreignkey')
        op.create_foreign_key('user_repos_repo_id_fkey', 'user_repos', 'repo', ['repo_id'], ['repo_id'], source_schema='augur_operations')
        op.alter_column('releases', 'release_id',
                existing_type=sa.CHAR(length=128),
                type_=sa.CHAR(length=256),
                existing_nullable=False,
                existing_server_default=sa.text('nextval(\'"augur_data".releases_release_id_seq\'::regclass)'),
                schema='augur_data')
        op.drop_table('repo_clones_data', schema='augur_data')