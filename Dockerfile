FROM python:3.q-slim

ENV_FILE .env

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code
WORKDIR = /code

CUR_DIRECTORY=/code/django_hello_world
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]