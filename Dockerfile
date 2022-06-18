# pull official base image
FROM python:3.10-alpine

ARG PG_PASS

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

RUN apk add --update git
RUN apk add --update py-pip

# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

ENV PG_PASS=$PG_PASS

# run gunicorn
CMD gunicorn world_cup.wsgi:application --bind 0.0.0.0:$PORT

