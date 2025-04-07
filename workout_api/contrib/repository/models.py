# repository/models.py

def import_models():
    """
    Importa e retorna os modelos utilizados na aplicação.
    
    Esta função é responsável por importar os modelos de diferentes módulos
    e retorná-los como uma tupla. Isso pode ser útil para centralizar a
    importação de modelos em um único local.
    """
    from workout_api.categorias.models import CategoriaModel
    from workout_api.atleta.models import AtletaModel
    from workout_api.centro_treinamento.models import CentroTreinamentoModel
    
    return CategoriaModel, AtletaModel, CentroTreinamentoModel