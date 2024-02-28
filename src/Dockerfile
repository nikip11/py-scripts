FROM python:3.9-alpine3.16
WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 1000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1000"]
