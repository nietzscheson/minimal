FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install -r requirements.txt
