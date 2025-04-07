from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from workout_api.configs.database import get_sessions

# Definindo uma dependência do FastAPI para injeção de sessão de banco de dados
DataBaseDependency = Annotated[AsyncSession, Depends(get_sessions)]