#!/usr/bin/env bash

DOMAIN=$(
    grep HOST_URL telegram_unvoicer_bot/settings.py | \
    tr " = ", "\n" | \
    tail -1
    )

openssl req \
    -newkey rsa:2048 \
    -sha256 \
    -nodes \
    -keyout nginx/certs/private.key \
    -x509 \
    -days 365 \
    -out nginx/certs/cert.pem \
    -subj "/C=US/ST=New York/L=Brooklyn/O=Unvoicer Company/CN=${DOMAIN:1:-1}"