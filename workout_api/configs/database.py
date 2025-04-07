from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from workout_api.configs.settings import settings

# Criando um mecanismo assíncrono para conexão com o banco de dados
engine = create_async_engine(settings.DB_URL, echo=False)

# Criando uma fábrica de sessões assíncronas
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_sessions() -> AsyncGenerator[AsyncSession, None]:
    """
    Gerador assíncrono que fornece uma sessão do banco de dados.
    
    Este gerador é utilizado para criar e gerenciar sessões de banco de dados
    de forma assíncrona, garantindo que a sessão seja fechada corretamente após o uso.
    """
    async with async_session() as session:
        yield session  # Fornece a sessão para uso