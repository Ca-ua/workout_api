from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Classe de configuração para o aplicativo.
    
    Esta classe utiliza Pydantic para gerenciar as configurações do aplicativo,
    incluindo a URL de conexão com o banco de dados.
    """
    # URL de conexão com o banco de dados, com um valor padrão
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:1423@localhost/workout')

# Instanciando a classe Settings para acessar as configurações
settings = Settings()