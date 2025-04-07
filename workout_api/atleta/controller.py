import datetime
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4

# Importando modelos e esquemas necessários
from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.repository.dependencies import DataBaseDependency

from sqlalchemy.future import select

# Criando um roteador para as rotas relacionadas a Atletas
router = APIRouter()


@router.post(
    "/",
    summary="Criar novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def post(db_session: DataBaseDependency, atleta_in: AtletaIn = Body(...)):
    """
    Cria um novo atleta no banco de dados.

    Verifica se a categoria e o centro de treinamento existem antes de criar o atleta.
    """
    # Obtendo os nomes da categoria e do centro de treinamento do atleta
    categoria_name = atleta_in.categoria.nome
    centro_treinamento_name = atleta_in.centro_treinamento.nome

    # Verificando se a categoria existe
    categoria = (
        (
            await db_session.execute(
                select(CategoriaModel).filter_by(nome=categoria_name)
            )
        )
        .scalars()
        .first()
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A categoria {categoria_name} não foi encontrada.",
        )

    # Verificando se o centro de treinamento existe
    centro_treinamento = (
        (
            await db_session.execute(
                select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_name)
            )
        )
        .scalars()
        .first()
    )

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_BAD_REQUEST,
            detail=f"O centro de treinamento {centro_treinamento_name} não foi encontrado.",
        )

    try:
        atleta_model = AtletaModel(
            nome=atleta_in.nome,
            cpf=atleta_in.cpf,
            idade=atleta_in.idade,
            peso=atleta_in.peso,
            altura=atleta_in.altura,
            sexo=atleta_in.sexo,
            categoria=categoria,
            centro_treinamento=centro_treinamento,
        )

        db_session.add(atleta_model)
        await db_session.commit()
        await db_session.refresh(atleta_model)

        return AtletaOut.model_validate(atleta_model)

    except Exception as e:
        print(f"Erro ao inserir no banco: {e}")  # boa pra debug
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Ocorreu um erro ao inserir os dados no banco.'
        )


@router.get(
    "/",
    summary="Consultar todos os Atletas",
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)
async def query(db_session: DataBaseDependency) -> list[AtletaOut]:
    """
    Consulta todos os atletas no banco de dados.
    """
    atletas: list[AtletaOut] = (
        (await db_session.execute(select(AtletaModel))).scalars().all()
    )

    return [AtletaOut.model_validate(atleta, from_attributes=True) for atleta in atletas]


@router.get(
    "/{id}",
    summary="Consultar Atleta por ID",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def query(id: int, db_session: DataBaseDependency) -> AtletaOut:
    """
    Consulta um atleta específico pelo ID.
    """
    atleta: AtletaOut = (
        (await db_session.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id {id}",
        )

    return atleta


@router.patch(
    "/{id}",
    summary="Editar um Atleta por ID",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def query(
    id: int, db_session: DataBaseDependency, atleta_up: AtletaUpdate = Body(...)
) -> AtletaOut:
    """
    Atualiza os dados de um atleta específico pelo ID.
    """
    atleta: AtletaOut = (
        (await db_session.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id {id}",
        )

    # Atualizando os dados do atleta com os novos valores
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)

    return atleta


@router.delete(
    "/{id}",
    summary="Deletar um Atleta por ID",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def query(id: int, db_session: DataBaseDependency) -> None:
    """
    Deleta um atleta específico pelo ID.
    """
    atleta: AtletaOut = (
        (await db_session.execute(select(AtletaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id {id}",
        )

    await db_session.delete(atleta)
    await db_session.commit()
