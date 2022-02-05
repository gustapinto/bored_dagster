"""create activities table

Revision ID: bc76d5f0d6a1
Revises:
Create Date: 2022-02-05 11:56:12.435675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc76d5f0d6a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'activities',
        sa.Column('id', sa.Integer, sa.Identity(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('kind', sa.String(50), nullable=False),
        sa.Column('participants', sa.SmallInteger, nullable=False),
        sa.Column('price', sa.DECIMAL(2), nullable=False)
    )


def downgrade():
    op.drop_table('activities')
