FROM python:3.10.6
RUN pip install fastapi uvicorn requests bs4 sqlalchemy psycopg2-binary flake8 isort black pre-commit email-validator
COPY . .
