FROM python:3.6-alpine3.14
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "app.py"]