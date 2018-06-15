#!/usr/bin/env bash

function getSettings {
    echo "$(
    grep $1 /telegram_unvoicer_bot/telegram_unvoicer_bot/settings.py | \
    tr " = ", "\n" | \
    tail -1
    )"
}

HOST_URL=$(getSettings HOST_URL)
WEBHOOKS_URL=$(getSettings WEBHOOKS_URL)
CERT_PATH=$(getSettings SSL_CERTIFICATES_PATH)
TOKEN=$(getSettings TELEGRAM_BOT_API_KEY)

curl \
    -F "url=https://${HOST_URL:1:-1}${WEBHOOKS_URL:1:-1}" \
    -F "certificate=@${CERT_PATH:1:-1}/cert.pem" \
    "https://api.telegram.org/bot${TOKEN:1:-1}/setWebhook"