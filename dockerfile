# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

CMD ["python", "api.py"]
