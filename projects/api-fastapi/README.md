# REST API — FastAPI + SQLite

API de cadastro construída para demonstrar backend aplicado: CRUD, validação, persistência e documentação automática.

## Endpoints

- `GET /health`
- `POST /contacts`
- `GET /contacts`
- `GET /contacts/{id}`
- `PUT /contacts/{id}`
- `DELETE /contacts/{id}`

## Stack

Python · FastAPI · SQLAlchemy · SQLite · Pydantic

## Executar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Documentação interativa:

`http://127.0.0.1:8000/docs`

## Decisões

- SQLite deixa o projeto simples e reproduzível localmente.
- SQLAlchemy separa a camada de persistência da API.
- Pydantic valida entrada e saída.
- O endpoint `/health` facilita monitoramento e deploy posterior.
