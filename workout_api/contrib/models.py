from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import uuid4

class BaseModel(DeclarativeBase):
    """
    Classe base para todos os modelos da aplicação.
    
    Esta classe herda de DeclarativeBase e fornece um identificador único
    (UUID) para todos os modelos que a utilizam. Os modelos que herdam
    de BaseModel terão um campo 'id' que é a chave primária.
    """
    # Identificador único do modelo (chave primária)
    id: Mapped[str] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)