FROM python:3.10.6
RUN pip install fastapi uvicorn requests bs4 sqlalchemy psycopg2-binary flake8 isort black pre-commit email-validator
COPY . .
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
