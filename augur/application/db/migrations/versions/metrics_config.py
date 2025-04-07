"""Add metrics_config table

Revision ID: metrics_config_001
Revises: None
Create Date: 2024-04-07

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision = 'metrics_config_001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create metrics_config table
    op.create_table('metrics_config',
        sa.Column('id', sa.Integer(), server_default=sa.text("nextval('augur_operations.metrics_config_id_seq'::regclass)"), nullable=False),
        sa.Column('section_name', sa.String(), nullable=False),
        sa.Column('metric_name', sa.String(), nullable=False),
        sa.Column('value', sa.String(), nullable=False),
        sa.Column('value_type', sa.String(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('units', sa.String(), nullable=True),
        sa.Column('valid_range', JSONB(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(precision=0), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(precision=0), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('section_name', 'metric_name', name='metrics_config_unique'),
        schema='augur_operations'
    )

    # Create sequence for id column
    op.execute("""
        CREATE SEQUENCE IF NOT EXISTS augur_operations.metrics_config_id_seq
        START WITH 1
        INCREMENT BY 1
        NO MINVALUE
        NO MAXVALUE
        CACHE 1
    """)

    # Insert initial metrics from Insight_Task section
    op.execute("""
        INSERT INTO augur_operations.metrics_config 
        (section_name, metric_name, value, value_type, description, valid_range)
        VALUES 
        ('Insight_Task', 'confidence_interval', '95', 'float', 'Confidence interval for statistical calculations', '{"min": 0, "max": 100}'),
        ('Insight_Task', 'contamination', '0.1', 'float', 'Contamination parameter for anomaly detection', '{"min": 0, "max": 1}'),
        ('Insight_Task', 'switch', '1', 'bool', 'Enable/disable switch for insight tasks', NULL),
        ('Insight_Task', 'workers', '1', 'int', 'Number of worker processes', '{"min": 1, "max": 32}'),
        ('Insight_Task', 'training_days', '1000', 'int', 'Number of days of data to use for training', '{"min": 1}'),
        ('Insight_Task', 'anomaly_days', '14', 'int', 'Number of days to look back for anomaly detection', '{"min": 1}')
    """)


def downgrade():
    # Drop metrics_config table
    op.drop_table('metrics_config', schema='augur_operations')
    
    # Drop sequence
    op.execute('DROP SEQUENCE IF EXISTS augur_operations.metrics_config_id_seq') 