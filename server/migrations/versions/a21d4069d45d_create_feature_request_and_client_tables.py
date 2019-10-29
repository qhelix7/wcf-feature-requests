"""create feature_request and client tables

Revision ID: a21d4069d45d
Revises: 
Create Date: 2019-10-21 11:39:14.588334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a21d4069d45d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('client',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feature_request',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=80), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=False),
        sa.Column('client_id', sa.Integer(), nullable=False),
        sa.Column(
            'priority',
            sa.Enum(
                'Undetermined',
                'Critical',
                'High',
                'Medium',
                'Low',
                name='priority_enum'
            ),
            nullable=False
        ),
        sa.Column('target_date', sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('feature_request')
    op.drop_table('client')
