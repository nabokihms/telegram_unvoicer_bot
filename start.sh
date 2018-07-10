#!/usr/bin/env bash

echo "All aboard!" \
    && telegram_unvoicer_bot_config_to_env -c "settings.yml" \
    && nginx \
    && telegram_unvoicer_bot_bind_webhook \
    && telegram_unvoicer_bot_start \
