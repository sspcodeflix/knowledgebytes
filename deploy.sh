#!/bin/bash

echo "Before Running This Script Make Sure To Create An ".env" File From ".env-sample" As Per Your Requirements."
sleep 20

echo "Starting MySQL Server..."
docker compose up mysql -d

echo "Waiting 60 Seconds For MYSQL Server Initialization..."
sleep 60

echo "Building & Starting Python Services..."
docker compose up python -d

echo "Waiting 60 Seconds For Python Services Initialization..."
sleep 60

echo "Initializing Nginx Server (HTTP Only) For SSL DNS Verification..."
docker compose up nginx-ssl-init -d

echo "Generating SSL Certificate With Certbot..."
docker compose up certbot -d

echo "Waiting 60 Seconds For Certbot To Complete SSL Generation & DNS Verification..."
sleep 60

echo "Stopping Nginx Server (HTTP only) Which Was Used For DNS Verification..."
docker compose down nginx-ssl-init

echo "Starting Production Nginx Server on (HTTP and HTTPS)..."
docker compose up nginx -d

echo "Deployment Completed Successfully"
