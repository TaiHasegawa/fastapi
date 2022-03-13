"""add last few dolumns to posts table

Revision ID: fa7c289aea19
Revises: fe21a7af143c
Create Date: 2022-03-13 17:03:20.467545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa7c289aea19'
down_revision = 'fe21a7af143c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
