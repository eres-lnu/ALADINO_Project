FROM ubuntu:16.04

MAINTAINER Sam "sam@sam.sam"

RUN apt-get update -y && \
	apt-get install -y python-pip python-dev python-mysqldb

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV DATABASE_URL "mysql://root:root@host.docker.internal:3306/database"

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]