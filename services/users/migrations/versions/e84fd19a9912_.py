"""empty message

Revision ID: e84fd19a9912
Revises: 2f3a16d13b1b
Create Date: 2018-12-12 16:13:23.933259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e84fd19a9912'
down_revision = '2f3a16d13b1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=True))
    op.execute('UPDATE users SET admin=False')
    op.alter_column('users', 'admin', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
