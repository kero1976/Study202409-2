FROM mysql:8.0-debian

RUN apt-get update
RUN apt-get install -y locales
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG=ja_JP.UTF-8

copy ./sql /docker-entrypoint-initdb.d

EXPOSE 3306
