import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool

from alembic import context
from workout_api.contrib.models import BaseModel
from workout_api.contrib.repository.models import *

# Configurações básicas do Alembic (extraídas do alembic.ini)
config = context.config

# Habilita o log com base no arquivo de configuração do Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define os metadados do projeto que o Alembic usará para gerar migrações
target_metadata = BaseModel.metadata


# Modo offline: gera os scripts SQL das migrações sem conectar ao banco
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# Modo online (sincrono): aplica migrações com uma conexão ativa
def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


# Modo online (assíncrono): aplica migrações usando engine async
async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


# Responsável por iniciar as migrações assíncronas com asyncio
def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


# Decide automaticamente se deve rodar as migrações em modo offline ou online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
