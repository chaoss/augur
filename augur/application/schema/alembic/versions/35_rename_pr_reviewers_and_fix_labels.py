"""Rename pull_request_reviewers table and fix pull_request_labels columns

Revision ID: 35
Revises: 34
Create Date: 2025-11-06 10:30:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '35'
down_revision = '34'
branch_labels = None
depends_on = None

def upgrade():
    # Rename pull_request_reviewers to pull_request_requested_reviewers
    op.rename_table('pull_request_reviewers', 'pull_request_requested_reviewers', schema='augur_data')
    
    # Rename the sequence
    op.execute('ALTER SEQUENCE augur_data.pull_request_reviewers_pr_reviewer_map_id_seq RENAME TO pull_request_requested_reviewers_pr_reviewer_map_id_seq')
    
    # Update the default value in the table
    op.execute('''
        ALTER TABLE augur_data.pull_request_requested_reviewers 
        ALTER COLUMN pr_reviewer_map_id 
        SET DEFAULT nextval('augur_data.pull_request_requested_reviewers_pr_reviewer_map_id_seq'::regclass)
    ''')
    
    # Fix column names in pull_request_labels
    with op.batch_alter_table('pull_request_labels', schema='augur_data') as batch_op:
        batch_op.alter_column('pr_src_id', 
                            new_column_name='pr_label_src_id',
                            existing_type=sa.BigInteger(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_src_node_id',
                            new_column_name='pr_label_node_id',
                            existing_type=sa.String(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_src_url',
                            new_column_name='pr_label_url',
                            existing_type=sa.String(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_src_description',
                            new_column_name='pr_label_description',
                            existing_type=sa.String(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_src_color',
                            new_column_name='pr_label_color',
                            existing_type=sa.String(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_src_default_bool',
                            new_column_name='pr_label_default_bool',
                            existing_type=sa.Boolean(),
                            existing_nullable=True)

def downgrade():
    # Revert pull_request_labels column names
    with op.batch_alter_table('pull_request_labels', schema='augur_data') as batch_op:
        batch_op.alter_column('pr_label_src_id',
                            new_column_name='pr_src_id',
                            existing_type=sa.BigInteger(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_label_node_id',
                            new_column_name='pr_src_node_id',
                            existing_type=sa.String(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_label_url',
                            new_column_name='pr_src_url',
                            existing_type=sa.String(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_label_description',
                            new_column_name='pr_src_description',
                            existing_type=sa.String(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_label_color',
                            new_column_name='pr_src_color',
                            existing_type=sa.String(),
                            existing_nullable=True)
        
        batch_op.alter_column('pr_label_default_bool',
                            new_column_name='pr_src_default_bool',
                            existing_type=sa.Boolean(),
                            existing_nullable=True)
    
    # Revert table name
    op.rename_table('pull_request_requested_reviewers', 'pull_request_reviewers', schema='augur_data')
    
    # Revert sequence name
    op.execute('ALTER SEQUENCE augur_data.pull_request_requested_reviewers_pr_reviewer_map_id_seq RENAME TO pull_request_reviewers_pr_reviewer_map_id_seq')
    
    # Update the default value in the table
    op.execute('''
        ALTER TABLE augur_data.pull_request_reviewers 
        ALTER COLUMN pr_reviewer_map_id 
        SET DEFAULT nextval('augur_data.pull_request_reviewers_pr_reviewer_map_id_seq'::regclass)
    ''')
