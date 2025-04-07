from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4
from sqlalchemy import select

# Importando modelos e esquemas necessários
from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.contrib.repository.dependencies import DataBaseDependency

# Criando um roteador para as rotas relacionadas a Categorias
router = APIRouter()

@router.post(
    '/',
    summary='Criar nova Categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_session: DataBaseDependency,
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    """
    Cria uma nova categoria no banco de dados.
    
    Recebe os dados da categoria, cria um novo registro e o salva no banco.
    """
    # Criando a saída da categoria com um novo ID gerado
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    
    # Criando o modelo da categoria para persistência no banco de dados
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    
    # Adicionando a nova categoria à sessão do banco de dados
    db_session.add(categoria_model)
    await db_session.commit()
    
    return categoria_out

@router.get(
    '/',
    summary='Consultar todas as Categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_session: DataBaseDependency) -> list[CategoriaOut]:
    """
    Consulta todas as categorias no banco de dados.
    
    Retorna uma lista de todas as categorias registradas.
    """
    # Executando a consulta para obter todas as categorias
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    
    return categorias

@router.get(
    '/{id}',
    summary='Consultar Categoria por ID',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query(id: UUID4, db_session: DataBaseDependency) -> CategoriaOut:
    """
    Consulta uma categoria específica pelo ID.
    
    Retorna os detalhes da categoria se encontrada, caso contrário, lança uma exceção.
    """
    # Executando a consulta para obter a categoria pelo ID
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Categoria não encontrada no id {id}'
        )
    
    return categoria