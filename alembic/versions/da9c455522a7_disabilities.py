"""disabilities

Revision ID: da9c455522a7
Revises: 3d45e98b9c12
Create Date: 2021-05-13 22:28:14.482549

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "da9c455522a7"
down_revision = "3d45e98b9c12"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("usertable", sa.Column("visual", sa.Boolean(), nullable=True))
    op.add_column("usertable", sa.Column("hearing", sa.Boolean(), nullable=True))
    op.add_column("usertable", sa.Column("speech_impediment", sa.Boolean(), nullable=True))
    op.add_column("usertable", sa.Column("locomotor", sa.Boolean(), nullable=True))
    op.add_column("usertable", sa.Column("neural", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("usertable", "neural")
    op.drop_column("usertable", "locomotor")
    op.drop_column("usertable", "speech_impediment")
    op.drop_column("usertable", "hearing")
    op.drop_column("usertable", "visual")
    # ### end Alembic commands ###
