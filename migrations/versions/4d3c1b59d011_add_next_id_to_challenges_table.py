"""Add next_id to Challenges table

Revision ID: 4d3c1b59d011
Revises: 6012fe8de495
Create Date: 2022-04-07 03:53:27.554190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4d3c1b59d011"
down_revision = "6012fe8de495"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("challenges", sa.Column("next_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        None, "challenges", "challenges", ["next_id"], ["id"], ondelete="SET NULL"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "challenges", type_="foreignkey")
    op.drop_column("challenges", "next_id")
    # ### end Alembic commands ###