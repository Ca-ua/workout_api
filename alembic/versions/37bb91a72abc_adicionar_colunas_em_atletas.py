"""Adicionar colunas em atletas

Revision ID: <ID GERADO>
Revises: 4ba3716a93a8
Create Date: <DATA>
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Preenche com os dados gerados pelo Alembic
revision: str = "<ID GERADO>"
down_revision: Union[str, None] = "4ba3716a93a8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("atletas", sa.Column("idade", sa.Integer(), nullable=True))
    op.add_column("atletas", sa.Column("peso", sa.Float(), nullable=True))
    op.add_column("atletas", sa.Column("altura", sa.Float(), nullable=True))
    op.add_column("atletas", sa.Column("sexo", sa.String(length=1), nullable=True))
    op.add_column(
        "atletas",
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_column("atletas", "idade")
    op.drop_column("atletas", "peso")
    op.drop_column("atletas", "altura")
    op.drop_column("atletas", "sexo")
    op.drop_column("atletas", "created_at")
