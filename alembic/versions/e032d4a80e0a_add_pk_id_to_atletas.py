"""Add pk_id to atletas

Revision ID: e032d4a80e0a
Revises: 1e76e079f442
Create Date: 2025-04-06 21:36:15.695840

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e032d4a80e0a"
down_revision: Union[str, None] = "1e76e079f442"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Adiciona a coluna pk_id se não existir
    with op.batch_alter_table("atletas") as batch_op:
        batch_op.add_column(
            sa.Column("pk_id", sa.Integer(), nullable=False, autoincrement=True)
        )
        batch_op.create_primary_key("pk_atletas", ["pk_id"])

    # Remover as restrições de chave estrangeira existentes
    op.drop_constraint("atletas_categoria_id_fkey", "atletas", type_="foreignkey")
    op.drop_constraint(
        "atletas_centro_treinamento_id_fkey", "atletas", type_="foreignkey"
    )

    # Criar novas chaves estrangeiras
    op.create_foreign_key(
        "fk_categoria", "atletas", "categorias", ["categoria_id"], ["pk_id"]
    )
    op.create_foreign_key(
        "fk_centro_treinamento",
        "atletas",
        "centros_treinamento",
        ["centro_treinamento_id"],
        ["id"],
    )

    # Adiciona a coluna pk_id na tabela categorias, se necessário
    with op.batch_alter_table("categorias") as batch_op:
        batch_op.add_column(
            sa.Column("pk_id", sa.Integer(), nullable=False, autoincrement=True)
        )
        batch_op.create_primary_key("pk_categorias", ["pk_id"])


def downgrade() -> None:
    # Remover a coluna pk_id da tabela atletas
    op.drop_column("atletas", "pk_id")

    # Remover a coluna pk_id da tabela categorias
    op.drop_column("categorias", "pk_id")

    # Recriar as restrições de chave estrangeira
    op.create_foreign_key(
        "atletas_categoria_id_fkey",
        "atletas",
        "categorias",
        ["categoria_id"],
        ["pk_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "atletas_centro_treinamento_id_fkey",
        "atletas",
        "centros_treinamento",
        ["centro_treinamento_id"],
        ["id"],
        ondelete="CASCADE",
    )
