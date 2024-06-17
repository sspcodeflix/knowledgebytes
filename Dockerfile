# Stage 2: Run
FROM python:3.10-slim
RUN mkdir /app
WORKDIR /app

# Install build essentials and other necessary packages
# Debian's apt package manager is used instead of Alpine's apk
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY . .

# Install the required packages in a single layer
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Cleanup unnecessary files
RUN rm -rf /app/__pycache__

EXPOSE 9090

# Use uWSGI to run the Flask app
#CMD ["uwsgi", "--http", ":9090", "--wsgi-file", "wsgi.py"]
#CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]

# Run Gunicorn
CMD ["gunicorn", "app:app", "-c", "gunicorn_config.py"]
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=9090"]


## Stage 2: Run
#FROM python:3.11-alpine
#RUN mkdir /app
#WORKDIR /app
## Install build essentials (including C compiler) and other necessary packages
#RUN apk add --no-cache build-base libffi-dev python3-dev linux-headers
#
#COPY requirements.txt .
#COPY . .
## Install the required packages in a single layer
#RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
#
## Optional: Remove build tools and cleanup unnecessary files
#RUN apk update && apk add --no-cache gcc musl-dev
#RUN rm -rf /var/cache/apk/*
#RUN rm -rf /app/__pycache__
#RUN apk del gcc musl-dev
#EXPOSE 9090
#
## Use uWSGI to run the Flask app
##CMD ["uwsgi", "--http", ":9090", "--wsgi-file", "wsgi.py"]
##CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
## Run Gunicorn
#CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:9090"]
##CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=9090"]