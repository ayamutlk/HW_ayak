"""add

Revision ID: 3dc899c91d46
Revises: b3de84a8e630
Create Date: 2023-01-31 17:11:45.021838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dc899c91d46'
down_revision = 'b3de84a8e630'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('video',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('video',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
