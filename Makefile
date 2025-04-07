# Comando para executar a aplicação FastAPI com Uvicorn
run:
	@uvicorn workout_api.main:app --reload

# Comando para criar migrações com Alembic
create-migrations:
	@set PYTHONPATH=%CD% && alembic revision --autogenerate -m $(d)