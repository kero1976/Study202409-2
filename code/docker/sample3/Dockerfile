FROM mysql:8.4

RUN microdnf update -y
RUN microdnf install -y glibc-locale-source
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8

ENV LANG=ja_JP.UTF-8

copy ./sql /docker-entrypoint-initdb.d

EXPOSE 3306
