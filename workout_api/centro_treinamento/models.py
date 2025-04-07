from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from typing import List  # Importando List do módulo typing

# Importando a classe base para os modelos
from workout_api.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    """
    Modelo que representa um Centro de Treinamento no banco de dados.
    
    Este modelo é mapeado para a tabela 'centros_treinamento' e contém informações
    sobre o centro de treinamento, incluindo um identificador único, nome, endereço
    e proprietário.
    """
    __tablename__ = 'centros_treinamento'

    # Identificador único do centro de treinamento (chave primária)
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True)
    
    # Nome do centro de treinamento (deve ser único e não pode ser nulo)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
    # Endereço do centro de treinamento (não pode ser nulo)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    
    # Nome do proprietário do centro de treinamento (não pode ser nulo)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    
    # Relacionamento com os atletas que pertencem a este centro de treinamento
    atletas: Mapped[List['AtletaModel']] = relationship(
        back_populates='centro_treinamento', 
        uselist=True
    )