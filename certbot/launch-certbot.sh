#!/bin/sh

set -e

wait_for_nginx() {
    until nc -z nginx 80; do
        echo "Waiting for nginx to be available..."
        sleep 5s
    done
    echo "Nginx is up and running."
}
issue_certificate() {
    certbot certonly \
        --webroot \
        --webroot-path "/vol/www/" \
        --domain "$DOMAIN" \
        --domain "www.$DOMAIN" \
        --email "$EMAIL" \
        --rsa-key-size 4096 \
        --agree-tos \
        --non-interactive
}
renew_certificate() {
    certbot renew \
        --webroot \
        --webroot-path "/vol/www/" \
        --rsa-key-size 4096 \
        --non-interactive
}
main() {
    wait_for_nginx
    echo "Checking for SSL/TLS certificate..."
    if [ -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ]; then
        echo "Certificate already exists. Renewing..."
        renew_certificate
    else
        echo "Certificate does not exist. Issuing a new one..."
        issue_certificate
    fi
    echo "Operation successful. Exiting..."
}
main
