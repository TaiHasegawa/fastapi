"""add user table

Revision ID: 340902c6dcec
Revises: a2f4ae7f7859
Create Date: 2022-03-13 16:41:43.231439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '340902c6dcec'
down_revision = 'a2f4ae7f7859'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                            server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"))
    pass


def downgrade():
    op.drop_table("users")
    pass
