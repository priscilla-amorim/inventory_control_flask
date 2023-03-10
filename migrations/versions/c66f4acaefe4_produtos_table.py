"""produtos table

Revision ID: c66f4acaefe4
Revises: 200907402ab9
Create Date: 2023-01-26 14:15:25.558152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c66f4acaefe4'
down_revision = '200907402ab9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=True),
    sa.Column('descricao', sa.String(length=128), nullable=True),
    sa.Column('unidade', sa.String(length=16), nullable=True),
    sa.Column('conservacao', sa.String(length=16), nullable=True),
    sa.Column('armazenamento', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produtos')
    # ### end Alembic commands ###
