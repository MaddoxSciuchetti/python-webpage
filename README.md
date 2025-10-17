# Python Webpage (Django)

A minimal Django site with a polished UI using Bootstrap 5 and production-ready static file handling via WhiteNoise. Configured for deployment on Vercel using a Python Serverless Function entrypoint.

## Local Development

- Python 3.11+
- Create a virtualenv and install deps:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
- Run migrations (optional if you will use topics/entries):
```bash
python manage.py migrate
```
- Start the dev server:
```bash
python manage.py runserver
```
- Collect static for production testing:
```bash
python manage.py collectstatic --noinput
```

## Project Structure
- `skeleton/` – Django project settings and URLs
- `handyman/` – App with templates and static assets
- `handyman/templates/handyman/` – `base.html`, `index.html`, `topics.html`, `topic.html`
- `handyman/static/handyman/css/style.css` – App stylesheet
- `api/index.py` – Vercel Python Serverless Function exposing Django WSGI app
- `vercel.json` – Vercel routing and build command

## Configuration
- `skeleton/settings.py` reads the following env vars:
  - `DJANGO_SECRET_KEY` – Secret key (recommended to set in production)
  - `DJANGO_DEBUG` – Set to `true` to enable debug
  - `DJANGO_ALLOWED_HOSTS` – Comma-separated hosts, defaults to `*`
- Static files:
  - `STATIC_URL=/static/`
  - `STATIC_ROOT=static`
  - Served with WhiteNoise; `collectstatic` outputs to `./static`

## Deploy to GitHub
- Commit and push the repository. `.gitignore` excludes build artifacts, SQLite DB, and virtualenvs.

## Deploy to Vercel
1. Ensure `requirements.txt` is present (it is) and includes Django + WhiteNoise.
2. Vercel detects Python from `api/index.py`.
3. `vercel.json` will:
   - Install requirements.
   - Run `python manage.py collectstatic --noinput` to build static assets into `/static`.
   - Route all requests to `api/index.py` (Django), and static assets under `/static/*` are served directly.
4. Add env vars in Vercel Project Settings:
   - `DJANGO_SECRET_KEY`: a secure random string
   - `DJANGO_DEBUG`: `false`
   - `DJANGO_ALLOWED_HOSTS`: your Vercel domain(s), e.g. `your-app.vercel.app`

## Notes
- SQLite is fine for demo use. On serverless, writes are ephemeral; the app guards DB access to avoid 500s if migrations/storage aren’t available.
- For a persistent DB, use a managed Postgres and configure `DATABASES` accordingly.
