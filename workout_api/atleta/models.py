from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import UUID
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone

# Importando a classe base para os modelos
from workout_api.contrib.models import BaseModel

class AtletaModel(BaseModel):
    """
    Modelo que representa um Atleta no banco de dados.
    
    Este modelo é mapeado para a tabela 'atletas' e contém informações
    sobre o atleta, incluindo dados pessoais e referências a categoria
    e centro de treinamento.
    """
    __tablename__ = 'atletas'

    # Identificador único do atleta (chave primária)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    # Nome do atleta
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    
    # CPF do atleta (deve ser único)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    
    # Idade do atleta
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    
    # Peso do atleta em kg
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Altura do atleta em metros
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Sexo do atleta (1 caractere)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    
    # Data de criação do registro do atleta
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

    # Relacionamento com a categoria do atleta
    categoria: Mapped['CategoriaModel'] = relationship(
        back_populates='atletas', 
        lazy='selectin'
    )
    
    # Identificador da categoria do atleta (chave estrangeira)
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey('categorias.pk_id'))
    
    # Relacionamento com o centro de treinamento do atleta
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(
        back_populates='atletas', 
        lazy='selectin'
    )
    
    # Identificador do centro de treinamento do atleta (chave estrangeira)
    centro_treinamento_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), 
        ForeignKey('centros_treinamento.id')
    )