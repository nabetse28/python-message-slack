FROM python:3.10.2

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt