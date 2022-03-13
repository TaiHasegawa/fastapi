"""create posts table

Revision ID: a33a08882c21
Revises: 
Create Date: 2022-03-13 16:24:10.287284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a33a08882c21'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                            sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
