# 🏋️‍♂️ Workout API — Sua Academia Digital com FastAPI

> 🚀 **Projeto final** do Bootcamp "Vivo - Python Backend Developer" da DIO  
> 💡 Desenvolvido por [Ca-ua](https://github.com/Ca-ua) com muito estudo, persistência e alguns `422 Unprocessable Entity` pelo caminho 😅

---

## 📌 Sobre o Projeto

A **Workout API** é uma aplicação desenvolvida em **Python com FastAPI**, voltada para o gerenciamento de **atletas**, **exercícios** e **fichas de treino**. O objetivo principal é praticar os fundamentos de desenvolvimento backend, desde a criação de rotas REST até a integração com banco de dados via ORM (SQLAlchemy).

---

## 🚧 Funcionalidades

- ✔️ **CRUD de Atletas**  
- ✔️ **CRUD de Exercícios**  
- ✔️ **Associação entre fichas e atletas**  
- ✔️ **Validações com Pydantic**  
- ✔️ **Integração com SQLite**  
- ✔️ **Documentação automática via Swagger e Redoc**

---

## 🚀 Como Rodar Localmente

### 1. Clone o Repositório

```bash
git clone https://github.com/Ca-ua/workout_api.git
cd workout_api
```
### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
```

### Windows:

```bash
venv\Scripts\activate
```

### Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Rode a Aplicação

```bash
uvicorn main:app --reload
```

### Estrutura do Projeto
```bash
workout_api/
├── main.py             # Ponto de entrada da aplicação
├── models/             # Modelos do banco de dados (SQLAlchemy)
├── routers/            # Rotas organizadas por entidade
├── schemas/            # Schemas de validação (Pydantic)
├── database/           # Conexão e configuração do banco
└── requirements.txt    # Dependências do projeto
```


