"""Add clients

Revision ID: 5a4f730f3cbf
Revises: a21d4069d45d
Create Date: 2019-10-23 18:59:21.690086

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '5a4f730f3cbf'
down_revision = 'a21d4069d45d'
branch_labels = None
depends_on = None


def upgrade():
    client_table = table(
        'client',
        column('name', String),
    )
    op.bulk_insert(
        client_table,
        [
            {'name': 'Client A'},
            {'name': 'Client B'},
            {'name': 'Client C'},
        ],
    )

def downgrade():
    pass
