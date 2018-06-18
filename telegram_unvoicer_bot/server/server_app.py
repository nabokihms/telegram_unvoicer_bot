import asyncio

from aiohttp import web
from telegram_unvoicer_bot.settings import WEBHOOKS_URL

from telegram_unvoicer_bot.telegram import TelegramWebhookHandler


@web.middleware
async def print_request(request, handler):
    print(await request.json())
    resp = await handler(request)
    return resp


def init_app() -> web.Application:
    webhook_handler = TelegramWebhookHandler(
        asyncio.get_event_loop()
    )

    a = web.Application(middlewares=[
        print_request,
    ])
    a.router.add_post(WEBHOOKS_URL, webhook_handler.handle)
    return a


app = init_app()
