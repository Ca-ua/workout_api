"""Recriar tabelas atletas e categorias

Revision ID: 4f7719f43564
Revises: 4dafd148dcdd
Create Date: 2025-04-06 23:13:38.930918
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "4f7719f43564"
down_revision: Union[str, None] = "4dafd148dcdd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ⚠️ Remove as tabelas antigas
    op.drop_table("atletas")
    op.drop_table("categorias")

    # 🆕 Recria a tabela categorias
    op.create_table(
        "categorias",
        sa.Column("pk_id", sa.Integer(), primary_key=True),
        sa.Column("nome", sa.String(), nullable=False),
    )

    # 🆕 Recria a tabela atletas
    op.create_table(
        "atletas",
        sa.Column("pk_id", sa.Integer(), primary_key=True),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("data_nascimento", sa.Date(), nullable=False),
        sa.Column(
            "categoria_id",
            sa.Integer(),
            sa.ForeignKey("categorias.pk_id"),
            nullable=False,
        ),
        sa.Column(
            "centro_treinamento_id",
            sa.UUID(),
            sa.ForeignKey("centros_treinamento.id"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    # ⚠️ Remove as tabelas recriadas
    op.drop_table("atletas")
    op.drop_table("categorias")

    # 🔁 Recria a tabela categorias como era antes (exemplo com UUID)
    op.create_table(
        "categorias",
        sa.Column("id", sa.UUID(), primary_key=True),
        sa.Column("nome", sa.String(), nullable=False),
    )

    # 🔁 Recria a tabela atletas com categoria_id como UUID
    op.create_table(
        "atletas",
        sa.Column("id", sa.UUID(), primary_key=True),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("data_nascimento", sa.Date(), nullable=False),
        sa.Column(
            "categoria_id", sa.UUID(), sa.ForeignKey("categorias.id"), nullable=False
        ),
        sa.Column(
            "centro_treinamento_id",
            sa.UUID(),
            sa.ForeignKey("centros_treinamento.id"),
            nullable=False,
        ),
    )
