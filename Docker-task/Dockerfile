FROM python:3.9-slim-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

FROM node:14.17.3

WORKDIR /app

COPY . /package*.json /app/

RUN npm install

COPY . /app/
