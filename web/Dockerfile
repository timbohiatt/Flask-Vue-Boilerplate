FROM node:lts-stretch-slim

ENV WAIT_VERSION 2.7.3

COPY ./web/package*.json ./web/node_modules /app/

COPY ./web/boot-app.sh /boot.sh
RUN chmod +x /boot.sh

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

WORKDIR /app

RUN npm install
