from typing import Annotated, Optional
from pydantic import BaseModel, Field, PositiveFloat

# Importando esquemas necessários
from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    """
    Esquema que representa um Atleta.
    
    Este esquema é utilizado para validar e documentar os dados do atleta,
    incluindo informações pessoais e referências a categoria e centro de treinamento.
    """
    nome: Annotated[str, Field(description='Nome do Atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M', max_length=1)]
    
    # Referência à categoria do atleta
    categoria: Annotated[CategoriaIn, Field(description='Categoria do Atleta')]
    
    # Referência ao centro de treinamento do atleta
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro Treinamento do Atleta')]

class AtletaIn(Atleta):
    """
    Esquema para entrada de dados de um novo Atleta.
    
    Este esquema herda de Atleta e é utilizado para validar os dados
    ao criar um novo atleta.
    """
    pass

class AtletaOut(Atleta, OutMixin):
    """
    Esquema para saída de dados de um Atleta.
    
    Este esquema herda de Atleta e OutMixin, e é utilizado para
    formatar os dados do atleta ao serem retornados pela API.
    """
    pass

class AtletaUpdate(BaseSchema):
    """
    Esquema para atualização de dados de um Atleta.
    
    Este esquema permite a atualização de campos específicos do atleta,
    onde os campos são opcionais.
    """
    nome: Annotated[Optional[str], Field(None, description='Nome do Atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do Atleta', example=25)]