FROM python:3.8.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install apscheduler pendulum requests

CMD python3 app.py