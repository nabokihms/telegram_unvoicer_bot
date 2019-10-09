import asyncio
import logging

from aiohttp import web

from telegram_unvoicer_bot.telegram import TelegramWebhookHandler


def init_app() -> web.Application:
    logging.basicConfig(level=logging.INFO)

    webhook_handler = TelegramWebhookHandler(
        asyncio.get_event_loop()
    )
    a = web.Application(middlewares=[])
    a.router.add_post('/webhooks', webhook_handler.handle)
    return a


app = init_app()
