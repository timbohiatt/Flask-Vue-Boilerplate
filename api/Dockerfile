FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV WAIT_VERSION 2.7.3

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./api/requirements.txt /requirements/requirements.txt
RUN pip install -r /requirements/requirements.txt

COPY ./api/boot-app.sh /boot.sh
RUN chmod +x /boot.sh

COPY ./api/boot-celery.sh /start-celeryworker.sh
RUN chmod +x /start-celeryworker.sh

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

WORKDIR /app