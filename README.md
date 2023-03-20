# NucScholar

## How to Run
### .env
```
DATABASE_DATABASE=
DATABASE_USER=
DATABASE_HOST=
DATABASE_PORT=
DATABASE_PASSWORD=

#postgres container
POSTGRES_USER=
POSTGRES_PASSWORD=

#pgadmin container
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
PGADMIN_PORT=8088
```

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`

### Backend
1. `python3 -m venv .venv`
2. `docker compose up -d`
3. `pip3 install -r backend/requirements.txt`
4. `python3 backend/manage.py runserver`
