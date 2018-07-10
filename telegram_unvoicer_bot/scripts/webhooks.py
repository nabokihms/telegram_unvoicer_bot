import asyncio
from os import getenv

from aiohttp import ClientSession

from telegram_unvoicer_bot.telegram import TelegramApiRequest

__all__ = [
    'bind_webhook',
    'get_webhook_info',
]


async def _curl_bind_webhook(loop):
    async with ClientSession(loop=loop) as session:
        resp = await TelegramApiRequest.post(
            'setWebhook', data={
                'url': f'https://${getenv("APP_DOMAIN")}/webhooks',
                'certificat': f'@${getenv("SSL_PATH")}/cert.pem',
            }
        )(session)
        print(
            await resp.json()
        )


async def _curl_get_webhook_info(loop):
    async with ClientSession(loop=loop) as session:
        resp = await TelegramApiRequest.get(
            'getWebhookinfo'
        )(session)
        print(
            await resp.json()
        )


def bind_webhook():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_curl_bind_webhook(loop))


def get_webhook_info():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_curl_get_webhook_info(loop))
