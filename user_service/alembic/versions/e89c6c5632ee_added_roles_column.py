"""added roles column

Revision ID: e89c6c5632ee
Revises: 83ba02c37f05
Create Date: 2025-06-20 18:27:49.065401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e89c6c5632ee'
down_revision: Union[str, Sequence[str], None] = '83ba02c37f05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.String(), nullable=False))
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
