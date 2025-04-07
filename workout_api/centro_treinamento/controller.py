from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4
from sqlalchemy import select

# Importando modelos e esquemas necessários
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.contrib.repository.dependencies import DataBaseDependency

# Criando um roteador para as rotas relacionadas a Centros de Treinamento
router = APIRouter()

@router.post(
    '/',
    summary='Criar um novo Centro de Treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DataBaseDependency,
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    """
    Cria um novo centro de treinamento no banco de dados.
    
    Recebe os dados do centro de treinamento, cria um novo registro e o salva no banco.
    """
    # Criando a saída do centro de treinamento com um novo ID gerado
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    
    # Criando o modelo do centro de treinamento para persistência no banco de dados
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    
    # Adicionando o novo centro de treinamento à sessão do banco de dados
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    
    return centro_treinamento_out

@router.get(
    '/',
    summary='Consultar todos os Centros de Treinamento',
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: DataBaseDependency) -> list[CentroTreinamentoOut]:
    """
    Consulta todos os centros de treinamento no banco de dados.
    
    Retorna uma lista de todos os centros de treinamento registrados.
    """
    # Executando a consulta para obter todos os centros de treinamento
    centros_treinamento: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    
    return centros_treinamento

@router.get(
    '/{id}',
    summary='Consultar Centro de Treinamento por ID',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_session: DataBaseDependency) -> CentroTreinamentoOut:
    """
    Consulta um centro de treinamento específico pelo ID.
    
    Retorna os detalhes do centro de treinamento se encontrado, caso contrário, lança uma exceção.
    """
    # Executando a consulta para obter o centro de treinamento pelo ID
    resultado = await db_session.execute(
        select(CentroTreinamentoModel).filter(CentroTreinamentoModel.id == id)
    )
    centro_treinamento = resultado.scalars().first()

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Centro de treinamento não encontrado no id {id}'
        )
    
    return centro_treinamento