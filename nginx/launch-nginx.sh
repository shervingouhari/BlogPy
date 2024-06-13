#!/bin/bash

set -e

configure_nginx() {
    echo "Checking for SSL/TLS certificate..."
    rm /etc/nginx/conf.d/default.conf
    if [ ! -f "/etc/letsencrypt/live/${DOMAIN}/fullchain.pem" ]; then
        echo "No SSL/TLS certification found, enabling HTTP only..."
        envsubst '${DOMAIN}' </etc/nginx/templates/default.conf >/etc/nginx/conf.d/default.conf
    else
        echo "SSL/TLS certification found, enabling HTTPS..."
        envsubst '${DOMAIN}' </etc/nginx/templates/default-ssl.conf >/etc/nginx/conf.d/default.conf
    fi
    echo "Nginx configuration completed."
}
generate_dhparams() {
    echo "Checking for dhparams.pem..."
    if [ ! -f "/etc/nginx/conf.d/ssl/ssl-dhparams.pem" ]; then
        echo "dhparams.pem does not exist - creating it..."
        openssl dhparam -out /etc/nginx/conf.d/ssl/ssl-dhparams.pem 2048
        echo "dhparams.pem created successfully."
    else
        echo "dhparams.pem already exists."
    fi
}
start_nginx() {
    echo "Starting Nginx..."
    nginx -g "daemon off;"
}
main() {
    configure_nginx
    generate_dhparams
    start_nginx
}
main
