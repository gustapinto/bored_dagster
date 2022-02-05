"""create activities table

Revision ID: bc76d5f0d6a1
Revises:
Create Date: 2022-02-05 11:56:12.435675

"""
from alembic import op
from sqlalchemy import Column, Integer, String, SmallInteger, DECIMAL


# revision identifiers, used by Alembic.
revision = 'bc76d5f0d6a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'activities',
        Column('id', Integer, primary_key=True),
        Column('name', String(100), nullable=False),
        Column('kind', String(50), nullable=False),
        Column('participants', SmallInteger, nullable=False),
        Column('price', DECIMAL(2), nullable=False)
    )


def downgrade():
    op.drop_table('activities')
