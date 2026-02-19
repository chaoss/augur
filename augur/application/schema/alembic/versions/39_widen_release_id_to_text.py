"""widen release_id column to Text

GitHub GraphQL node IDs for tags/releases are base64 strings that can
exceed the original CHAR(128) / CHAR(64) limit seen in older installs.
Change the column to Text so any length ID can be stored.

Revision ID: 39
Revises: 38
Create Date: 2026-02-19
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39'
down_revision = '38'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'releases',
        'release_id',
        existing_type=sa.CHAR(),
        type_=sa.Text(),
        schema='augur_data',
    )


def downgrade():
    op.alter_column(
        'releases',
        'release_id',
        existing_type=sa.Text(),
        type_=sa.CHAR(length=128),
        schema='augur_data',
    )
