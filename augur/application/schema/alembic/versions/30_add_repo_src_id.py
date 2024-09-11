"""Add repo src id

Revision ID: 30
Revises: 29
Create Date: 2024-08-30

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '30'
down_revision = '29'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('repo', sa.Column('repo_src_id', sa.BigInteger(), nullable=True), schema='augur_data')
    op.create_unique_constraint('repo_src_id_unique', 'repo', ['repo_src_id'], schema='augur_data')
    

def downgrade():
    op.drop_constraint('repo_src_id_unique', 'repo', schema='augur_data', type_='unique')
    op.drop_column('repo', 'repo_src_id', schema='augur_data')
