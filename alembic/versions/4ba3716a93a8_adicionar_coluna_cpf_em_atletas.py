"""Adicionar coluna cpf em atletas

Revision ID: 4ba3716a93a8
Revises: 4f7719f43564
Create Date: 2025-04-06 23:39:31.838211
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4ba3716a93a8"
down_revision: Union[str, None] = "4f7719f43564"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("atletas", sa.Column("cpf", sa.String(length=14), nullable=True))


def downgrade() -> None:
    op.drop_column("atletas", "cpf")
