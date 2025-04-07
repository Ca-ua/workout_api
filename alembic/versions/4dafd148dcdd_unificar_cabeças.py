"""Unificar cabeças

Revision ID: 4dafd148dcdd
Revises: xxxx, e032d4a80e0a
Create Date: 2025-04-06 22:51:37.965028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dafd148dcdd'
down_revision: Union[str, None] = ('xxxx', 'e032d4a80e0a')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
