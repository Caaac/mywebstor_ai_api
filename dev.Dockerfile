FROM python:3.12-slim

WORKDIR /app

COPY ./requirements/dev.txt ./requirements.txt

RUN pip install --upgrade pip==25.1.1

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8010
