#!/bin/bash

echo "Stopping Production Nginx (HTTP and HTTPS)..."
docker compose -f deploy/docker-compose-nginx.yaml down

echo "Stopping Python services..."
docker compose -f docker-compose.yaml down

echo "Stopping MySQL..."
docker compose -f deploy/mysql/docker-compose.yaml down

echo "Stopping Certbot..."
docker compose -f deploy/docker-compose-certbot.yaml down

echo "All Services Stopped Successfully."
