# FastAPI — video game marketplace

REST API and web client for a digital video game marketplace. A user browses the catalog, buys, reviews, tags games (at most 5 tags per user and game), and manages a subscription.

## What's here

The backend is **FastAPI** with SQLAlchemy. The frontend is a **Create React App** in `frontend/` (login, register, library, tags, reviews, profile, and user admin).

### Models

`ElementVenda`, `Videojoc`, `DLC`, `Venda`, `Usuari`, `Etiqueta`, `EtiquetaCom`, `Opinio`, `Subscripcio`, `Acces`.

### Routes

Under `backend/app/router/`:

- `videojoc`, `dlc`, `elementvenda`
- `venda`, `usuari`, `acces`
- `etiqueta`, `opinio`, `subscripcio`

The API entry point is `backend/app/main.py`. The database URL is read in `backend/app/config.py` / `backend/app/database.py`.

## Requirements

- Python 3.9 or newer
- PostgreSQL
- Node.js for the frontend

## Backend

From the repository root:

```bash
pip install -r requirements.txt
```

Set the PostgreSQL connection in `backend/app/database.py` (user, password, host, and database name). Then:

```bash
uvicorn backend.app.main:app --reload
```

Interactive docs are at `http://127.0.0.1:8000/docs`.

## Frontend

```bash
cd frontend
npm install
npm start
```

The client must point at the URL where Uvicorn is listening. That address is in the frontend code (for example in `src/appInstance.jsx`).

## Layout

```
backend/app/
├── main.py
├── config.py
├── database.py
├── models/
├── schemas/
├── crud/
└── router/
frontend/src/
├── Login.js
├── Register.js
├── Catalog.js
├── Componentes/
└── rutas/          # library, tags, reviews, profile, users
requirements.txt
```
