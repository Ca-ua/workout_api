from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List  # Importando List do módulo typing

# Importando a classe base para os modelos
from workout_api.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    """
    Modelo que representa uma Categoria no banco de dados.
    
    Este modelo é mapeado para a tabela 'categorias' e contém informações
    sobre a categoria, incluindo um identificador único e o nome da categoria.
    """
    __tablename__ = 'categorias'

    # Identificador único da categoria (chave primária)
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    
    # Nome da categoria (deve ser único e não pode ser nulo)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
    # Relacionamento com os atletas que pertencem a esta categoria
    atletas: Mapped[List['AtletaModel']] = relationship(
        back_populates='categoria', 
        uselist=True
    )