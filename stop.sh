#!/bin/bash

echo "Stopping Production Nginx Server (HTTP and HTTPS)..."
docker compose down nginx

echo "Stopping Python services..."
docker compose down python

echo "Stopping MySQL Server..."
docker compose down mysql

echo "Stopping Certbot..."
docker compose down certbot

echo "Stopping Nginx (HTTP Only) if it's Running..."
docker compose down nginx-ssl-init

echo "All Services Stopped Successfully."
