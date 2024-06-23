#!/bin/bash

echo "Starting MySQL..."
cd deploy/mysql/ && cp .env-sample .env && docker compose up -d

echo "Waiting For 30 Seconds For MYSQL Initialization..."
sleep 30

echo "Starting Python Services..."
cd ../.. && cp .env-sample .env && docker compose up -d

echo "Initializing Nginx On HTTP For SSL DNS Verification..."
cd deploy && docker compose -f docker-compose-nginx-ssl-init.yaml up -d

echo "Generating SSL Certificate With Certbot..."
docker compose -f docker-compose-certbot.yaml up -d

echo "Waiting 60 Seconds For Certbot To Complete SSL Generation & DNS Verification..."
sleep 60

echo "Stopping Nginx (HTTP only) Which Was Used For DNS Verification..."
docker compose -f docker-compose-nginx-ssl-init.yaml down

echo "Starting Production Nginx (HTTP and HTTPS)..."
docker compose -f docker-compose-nginx.yaml up -d

echo "Deployment Completed Successfully"
