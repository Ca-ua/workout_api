from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime

class BaseSchema(BaseModel):
    """
    Classe base para todos os esquemas da aplicação.
    
    Esta classe herda de BaseModel do Pydantic e configura as opções
    para validação de dados. A configuração 'extra' proíbe campos não
    definidos e 'from_attributes' permite a criação de instâncias a partir
    de atributos de objetos.
    """
    class Config:
        extra = 'forbid'  # Proíbe campos não definidos
        from_attributes = True  # Permite a criação a partir de atributos

class OutMixin(BaseSchema):
    """
    Mixin para esquemas de saída que incluem campos comuns.
    
    Este mixin adiciona campos comuns de identificação e data de criação
    a outros esquemas que o utilizam.
    """
    id: Annotated[int, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de criação')]