# FastAPI — mercat de videojocs

API REST i client web per a un mercat digital de videojocs. L'usuari consulta el catàleg, compra, opina, etiqueta (com a màxim 5 etiquetes per usuari i videojoc) i gestiona la subscripció.

## Què hi ha

El backend és **FastAPI** amb SQLAlchemy. El frontend és una app **Create React App** a `frontend/` (login, registre, biblioteca, etiquetes, opinions, perfil i administració d'usuaris).

### Models

`ElementVenda`, `Videojoc`, `DLC`, `Venda`, `Usuari`, `Etiqueta`, `EtiquetaCom`, `Opinio`, `Subscripcio`, `Acces`.

### Rutes

Sota `backend/app/router/`:

- `videojoc`, `dlc`, `elementvenda`
- `venda`, `usuari`, `acces`
- `etiqueta`, `opinio`, `subscripcio`

L'entrada de l'API és `backend/app/main.py`. La URL de la base es llegeix a `backend/app/config.py` / `backend/app/database.py`.

## Requisits

- Python 3.9 o superior
- PostgreSQL
- Node.js per al frontend

## Backend

Des de l'arrel del repositori:

```bash
pip install -r requirements.txt
```

Configura la connexió a PostgreSQL a `backend/app/database.py` (usuari, contrasenya, host i nom de la base). Després:

```bash
uvicorn backend.app.main:app --reload
```

La documentació interactiva queda a `http://127.0.0.1:8000/docs`.

## Frontend

```bash
cd frontend
npm install
npm start
```

El client ha d'apuntar a la URL on escolta Uvicorn. Aquesta adreça està al codi del frontend (per exemple a `src/appInstance.jsx`).

## Estructura

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
└── rutas/          # biblioteca, etiquetes, opinions, perfil, usuaris
requirements.txt
```
