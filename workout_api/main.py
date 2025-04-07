from fastapi import FastAPI
from workout_api.routers import api_router

# Criando uma instância da aplicação FastAPI
app = FastAPI(title="WorkoutApi")

# Incluindo o roteador principal da API
app.include_router(api_router)