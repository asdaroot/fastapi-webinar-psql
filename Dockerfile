FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get  update 
RUN apt-get install -y net-tools

EXPOSE 8000
WORKDIR /app

COPY . /app
RUN pip install -e .

