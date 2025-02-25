"""changed role for user

Revision ID: ddc9a3d5ce01
Revises: 29f57164950f
Create Date: 2024-12-30 14:34:22.243181

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ddc9a3d5ce01'
down_revision: Union[str, None] = '29f57164950f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=postgresql.ENUM('admin', 'user', name='user_role_enum'),
               nullable=True,
               existing_server_default=sa.text("'user'::user_role_enum"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'role',
               existing_type=postgresql.ENUM('admin', 'user', name='user_role_enum'),
               nullable=False,
               existing_server_default=sa.text("'user'::user_role_enum"))
    # ### end Alembic commands ###
