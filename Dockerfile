FROM python:3.10.6
RUN pip install fastapi uvicorn requests bs4 sqlalchemy psycopg2-binary flake8 isort black pre-commit
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]



# FROM python:3.10.6
# ENV APP_HOME /app
# COPY . .
# RUN pip install fastapi uvicorn requests bs4 sqlalchemy psycopg2-binary flake8 isort black pre-commit
# EXPOSE 8000
# RUN pip install pipenv
# RUN pipenv install --deploy --system
# RUN pip install pipenv
# RUN pipenv install --deploy --system
# CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app
