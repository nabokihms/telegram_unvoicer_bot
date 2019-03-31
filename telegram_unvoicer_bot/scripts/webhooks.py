import asyncio
from os import getenv

from aiohttp import ClientSession

from telegram_unvoicer_bot.telegram import telegram_api_get_webhookinfo, \
    telegram_api_set_webhook

__all__ = [
    'bind_webhook',
    'get_webhook_info',
]


async def _curl_bind_webhook(loop):
    app_domain = getenv('APP_DOMAIN')
    if app_domain is None:
        print('Environ APP_DOMAIN is not set.')
        return
    
    certificate = getenv('SSL_PATH')
    if certificate is None:
        print('Environ SSL_PATH is not set.')
        return
    
    async with ClientSession(loop=loop) as session:
        resp = await telegram_api_set_webhook(
            session, data={
                'url': f'https://${getenv("APP_DOMAIN")}/webhooks',
                'certificate': f'@${getenv("SSL_PATH")}/cert.pem',
            }
        )
        print(await resp.json())


async def _curl_get_webhook_info(loop):
    async with ClientSession(loop=loop) as session:
        resp = await telegram_api_get_webhookinfo(session)
        print(await resp.json())


def bind_webhook():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_curl_bind_webhook(loop))


def get_webhook_info():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_curl_get_webhook_info(loop))
