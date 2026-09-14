# data-service

Service de données, exposition des datamarts AN, Sénat, Parlement européen.

Django + Django REST Framework, PostgreSQL, géré avec [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv sync
cp .env.example .env    # ajuster JWT_PUBLIC_KEY, DATABASE_URL, etc.
git config core.hooksPath .githooks   # active les hooks locaux (une fois)
uv run python manage.py migrate
uv run python manage.py runserver
```

`GET /api/health/` → `{"status": "ok"}`

## Authentification

data-service ne fait que **vérifier** les JWT émis par `auth-service` (RS256) :
il détient uniquement `JWT_PUBLIC_KEY` (jamais la clé privée). Voir
`auth-service/README.md` pour la génération de la paire de clés.
