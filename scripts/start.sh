#!/usr/bin/env bash

echo "All aboard!" \
    && bash -c "/telegram_unvoicer_bot/scripts/set_webhook.sh" \
    && nginx \
    && telegram_unvoicer_bot_start