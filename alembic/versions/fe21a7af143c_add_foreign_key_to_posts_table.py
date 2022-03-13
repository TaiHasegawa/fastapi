"""add foreign-key to posts table

Revision ID: fe21a7af143c
Revises: 340902c6dcec
Create Date: 2022-03-13 16:55:24.142329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe21a7af143c'
down_revision = '340902c6dcec'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users",
                        local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")

    pass
