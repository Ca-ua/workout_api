from fastapi import APIRouter
from workout_api.atleta.controller import router as atleta
from workout_api.categorias.controller import router as categorias
from workout_api.centro_treinamento.controller import router as centro_treinamento

# Criando um roteador principal para a API
api_router = APIRouter()

# Incluindo o roteador de atletas com um prefixo e tags
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])

# Incluindo o roteador de categorias com um prefixo e tags
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])

# Incluindo o roteador de centro de treinamento com um prefixo e tags
api_router.include_router(centro_treinamento, prefix='/centro_treinamento', tags=['centro_treinamento'])