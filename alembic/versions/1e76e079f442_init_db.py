"""init_db

Revision ID: 1e76e079f442
Revises: 
Create Date: 2025-04-02 21:55:50.601567

Migration responsável por criar as tabelas iniciais do banco de dados:
- categorias
- centros_treinamento
- atletas
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid

# Identificadores obrigatórios do Alembic para controle de versão
revision: str = '1e76e079f442'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Aplica a migration:
    Cria as tabelas principais do domínio da aplicação.
    """

    # Tabela de categorias dos atletas (Ex: Infantil, Adulto, Profissional)
    op.create_table('categorias',
        sa.Column('id', sa.UUID(), primary_key=True, default=uuid.uuid4, nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False, unique=True)
    )

    # Tabela de centros de treinamento onde os atletas treinam
    op.create_table('centros_treinamento',
        sa.Column('id', sa.UUID(), primary_key=True, default=uuid.uuid4, nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False, unique=True),
        sa.Column('endereco', sa.String(length=60), nullable=False),
        sa.Column('proprietario', sa.String(length=30), nullable=False)
    )

    # Tabela de atletas com dados pessoais e vínculos com categoria e centro de treinamento
    op.create_table('atletas',
        sa.Column('id', sa.UUID(), primary_key=True, default=uuid.uuid4, nullable=False),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('cpf', sa.String(length=11), nullable=False, unique=True),
        sa.Column('idade', sa.Integer(), nullable=False),
        sa.Column('peso', sa.Float(), nullable=False),
        sa.Column('altura', sa.Float(), nullable=False),
        sa.Column('sexo', sa.String(length=1), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False),

        # Relações com FK e delete em cascata
        sa.Column('categoria_id', sa.UUID(), sa.ForeignKey('categorias.id', ondelete="CASCADE"), nullable=False),
        sa.Column('centro_treinamento_id', sa.UUID(), sa.ForeignKey('centros_treinamento.id', ondelete="CASCADE"), nullable=False)
    )


def downgrade() -> None:
    """
    Reverte a migration:
    Remove as tabelas criadas na ordem correta para evitar conflitos de chave estrangeira.
    """
    op.drop_table('atletas')
    op.drop_table('centros_treinamento')
    op.drop_table('categorias')
