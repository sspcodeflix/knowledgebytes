FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

EXPOSE 5000

RUN flask db upgrade

RUN mkdir -p gunicorn-logs

CMD ["gunicorn", "-c", "gunicorn_config.py", "run:app", "--access-logfile", "gunicorn-logs/access.log", "--error-logfile", "gunicorn-logs/error.log"]
