"""add content column to posts table

Revision ID: a2f4ae7f7859
Revises: a33a08882c21
Create Date: 2022-03-13 16:36:36.603642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f4ae7f7859'
down_revision = 'a33a08882c21'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
