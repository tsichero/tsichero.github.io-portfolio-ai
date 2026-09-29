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

## Evidências

- [Mapa dos endpoints e status de teste](output/openapi.json)
- [Evidência funcional](output/evidence.md)

A suíte validada cobre health check, criação, listagem e tratamento de recurso inexistente.
