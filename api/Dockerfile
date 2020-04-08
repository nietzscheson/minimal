FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev nodejs nodejs-npm

RUN npm install -g firebase-tools@latest serverless

RUN pip3 install --upgrade pip

RUN pip3 install awscli --upgrade --user --no-warn-script-locatio

COPY requirements.txt .

RUN pip3 install -r requirements.txt
