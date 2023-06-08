# FROM python:3.8.0-alpine
# 
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# 
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev
# 
# RUN pip3 install --upgrade pip
# 
# WORKDIR /usr/src/app
# 
# COPY requirements.txt .
# 
# RUN pip3 install -r requirements.txt


   
FROM python:3.9.2 as python-base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN pip install --upgrade pip

RUN pip install poetry==1.2.0a2

WORKDIR /home/core

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-root --no-dev

FROM python-base as development

RUN pip install pre-commit

RUN poetry install

COPY . ./

# CMD flask db upgrade; flask run --host 0.0.0.0 
CMD python minimal.py runserver 0:8000