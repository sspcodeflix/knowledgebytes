#!/bin/sh

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
ENV_FILE="$SCRIPT_DIR/.env"
source "$ENV_FILE"
trap exit TERM
while :
do
  certbot certonly --webroot -w /var/www/certbot -d "${HOSTNAME}" --email "${EMAIL}" --rsa-key-size 2048 --agree-tos --non-interactive --force-renewal
  sleep 12h & wait $!
done

