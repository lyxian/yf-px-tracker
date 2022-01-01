# Yahoo-Fianace-Price-Tracker

**Docker Command**
docker build -t yf-px-tracker:1
docker run --rm -d -v "$PWD/logs:/app/logs" --name yf-px-tracker yf-px-tracker:1

**Packages**
apscheduler
pendulum
requests
