from typing import Annotated
from pydantic import UUID4, Field

# Importando a classe base para os esquemas
from workout_api.contrib.schemas import BaseSchema

class CategoriaIn(BaseSchema):
    """
    Esquema para entrada de dados de uma nova Categoria.
    
    Este esquema é utilizado para validar e documentar os dados da categoria
    ao criar uma nova categoria.
    """
    nome: Annotated[str, Field(description='Nome da Categoria', example='Scale', max_length=10)]

class CategoriaOut(CategoriaIn):
    """
    Esquema para saída de dados de uma Categoria.
    
    Este esquema herda de CategoriaIn e é utilizado para formatar os dados
    da categoria ao serem retornados pela API, incluindo o identificador único.
    """
    id: Annotated[UUID4, Field(description='Identificador da categoria')]