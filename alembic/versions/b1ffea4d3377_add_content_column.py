"""add content column

Revision ID: b1ffea4d3377
Revises: bcf61a7c5ede
Create Date: 2023-06-25 07:18:59.310930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1ffea4d3377'
down_revision = 'bcf61a7c5ede'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('detail', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'detail')
    pass
