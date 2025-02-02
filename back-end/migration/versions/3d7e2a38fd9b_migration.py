"""migration

Revision ID: 3d7e2a38fd9b
Revises: 
Create Date: 2024-07-03 00:45:33.293345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = '3d7e2a38fd9b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('certificates',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('nome_coordenador', sa.String(), nullable=True),
    sa.Column('nome_curso', sa.String(), nullable=True),
    sa.Column('carga_horaria', sa.Integer(), nullable=True),
    sa.Column('data_conclusao', sa.String(), nullable=True),
    sa.Column('descricao', sa.String(), nullable=True),
    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('certificates')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
