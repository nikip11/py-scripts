FROM python:3.9-alpine3.16
WORKDIR /app

COPY ./src /app/src
COPY ./src/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
WORKDIR /app/app

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_config.py", "app.main:app"]
