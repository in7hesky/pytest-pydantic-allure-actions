FROM python:3.13.1-slim-bookworm

WORKDIR /framework

COPY ./requirements.txt /framework

RUN pip install --no-cache-dir -r requirements.txt
