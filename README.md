# TrendSphere (Flask Blog)

A production-ready Flask blogging site scaffold with SEO, monetization, and dynamic homepage.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
flask db init && flask db migrate -m "init" && flask db upgrade
flask run
```

Open http://localhost:5000

## Environment

Copy `.env.example` to `.env` and set values.

## Deploy

Run with Gunicorn:

```bash
gunicorn -c gunicorn.conf.py wsgi:app
```
