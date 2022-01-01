FROM python:3.10.1-slim-buster

WORKDIR /app

COPY . /app

RUN pip install apscheduler pendulum requests

CMD python3 app.py