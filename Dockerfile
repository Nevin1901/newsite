# FROM nginx/unit:1.20.0-python3

FROM python:3

WORKDIR /www/app

EXPOSE 8000

COPY requirements.txt /config/requirements.txt
RUN apt-get update && pip3 install flask gunicorn requests && rm -rf /var/lib/apt/lists/*

# COPY config.json /docker-entrypoint.d/config.json

COPY . .

CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:8000", "app"]
