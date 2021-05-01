FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps \
    nodejs yarn nodejs-npm \ 
    && rm -rf /var/cache/apk/*

RUN npm install serverless serverless-python-requirements serverless-wsgi -g

RUN pip3 install --upgrade pip 

RUN pip3 install awscli --upgrade --user --no-warn-script-location

RUN cp /root/.local/bin/aws /usr/bin/aws && chmod -R a+w /usr/bin/aws

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt
