from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

revision = 'xxxx'  # Substitua pelo ID gerado
down_revision = None  # Se esta for a primeira migração
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Criar tabela categorias
    op.create_table(
        'categorias',
        sa.Column('pk_id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(50), unique=True, nullable=False)
    )

    # Criar tabela centros_treinamento
    op.create_table(
        'centros_treinamento',
        sa.Column('id', PG_UUID(as_uuid=True), primary_key=True),
        sa.Column('nome', sa.String(50), unique=True, nullable=False),
        sa.Column('endereco', sa.String(60), nullable=False),
        sa.Column('proprietario', sa.String(30), nullable=False)
    )

    # Criar tabela atletas
    op.create_table(
        'atletas',
        sa.Column('pk_id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('cpf', sa.String(11), unique=True, nullable=False),
        sa.Column('idade', sa.Integer(), nullable=False),
        sa.Column('peso', sa.Float(), nullable=False),
        sa.Column('altura', sa.Float(), nullable=False),
        sa.Column('sexo', sa.String(1), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('categoria_id', sa.Integer(), sa.ForeignKey('categorias.pk_id')),
        sa.Column('centro_treinamento_id', PG_UUID(as_uuid=True), sa.ForeignKey('centros_treinamento.id'))
    )

def downgrade() -> None:
    op.drop_table('atletas')
    op.drop_table('centros_treinamento')
    op.drop_table('categorias')