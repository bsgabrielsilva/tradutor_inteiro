FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /numerosExtenso
WORKDIR /numerosExtenso

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /numerosExtenso/

RUN pip install -r /numerosExtenso/requirements.txt

ADD . /numerosExtenso/

# Django service
EXPOSE 8000