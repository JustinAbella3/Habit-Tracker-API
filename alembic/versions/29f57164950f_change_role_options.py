"""change role options

Revision ID: 29f57164950f
Revises: afa764b0f7a9
Create Date: 2024-12-30 12:48:43.537627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '29f57164950f'
down_revision: Union[str, None] = 'afa764b0f7a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
      # Create new enum type
    op.drop_column('users', 'role')
    
    # Create a new enum type for role
    role_enum = postgresql.ENUM('admin', 'user', name='user_role_enum')
    role_enum.create(op.get_bind())
    
    # Add the new role column with the enum type
    op.add_column('users', sa.Column('role', sa.Enum('admin', 'user', name='user_role_enum'), nullable=False, server_default='user'))




def downgrade() -> None:
    # Drop the new role column
    op.drop_column('users', 'role')
    
    # Drop the enum type
    op.execute('DROP TYPE user_role_enum')
    
    # Recreate the original role column (adjust the type as needed)
    op.add_column('users', sa.Column('role', sa.String(50)))
