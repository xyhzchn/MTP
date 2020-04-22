"""del relateCases column,use caseorder to replace

Revision ID: 1c9ced73e54e
Revises: f4a396769214
Create Date: 2016-04-27 19:54:23.201736

"""

# revision identifiers, used by Alembic.
revision = '1c9ced73e54e'
down_revision = 'f4a396769214'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('testjob', 'relateCases')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('testjob', sa.Column('relateCases', sa.BLOB(), nullable=True))
    ### end Alembic commands ###
