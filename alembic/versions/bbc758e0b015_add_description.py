"""add description

Revision ID: bbc758e0b015
Revises: d710d7cbba58
Create Date: 2021-05-08 18:48:46.645469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbc758e0b015'
down_revision = 'd710d7cbba58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usertable', sa.Column('description', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usertable', 'description')
    # ### end Alembic commands ###