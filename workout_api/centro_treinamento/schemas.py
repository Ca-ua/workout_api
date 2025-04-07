from typing import Annotated
from pydantic import UUID4, Field

# Importando a classe base para os esquemas
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    """
    Esquema para entrada de dados de um novo Centro de Treinamento.
    
    Este esquema é utilizado para validar e documentar os dados do centro de treinamento
    ao criar um novo registro.
    """
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua X, Q02', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Lira', max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    """
    Esquema para representar um Centro de Treinamento em contexto de Atleta.
    
    Este esquema é utilizado para retornar informações do centro de treinamento
    associado a um atleta.
    """
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    """
    Esquema para saída de dados de um Centro de Treinamento.
    
    Este esquema herda de CentroTreinamentoIn e é utilizado para formatar os dados
    do centro de treinamento ao serem retornados pela API, incluindo o identificador único.
    """
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento', example='e7bfc416-b0e2-4e69-8a0f-1216e1a3f9d2')]