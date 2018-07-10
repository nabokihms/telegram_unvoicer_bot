from json import dumps
from operator import methodcaller
from typing import Dict

from aiohttp import ClientResponse, ClientSession

from .const import TELEGRAM_BOT_API_URL

__all__ = [
    'telegram_api_get_file_method',
    'telegram_api_send_message',
    'telegram_api_get_webhookinfo',
    'telegram_api_set_webhook',
]


_ALLOWED_HTTP_METHODS = {'get', 'post'}


class _TelegramApiRequestBuilder(object):
    """
    Класс для создания запросов на API телеграма.
    """
    def __init__(self, http_method: str, api_method: str):
        lowered_http_method = http_method.lower()

        assert lowered_http_method in _ALLOWED_HTTP_METHODS, \
            f'Недопустимый http метод - {lowered_http_method}.'

        self._http_method = lowered_http_method
        self._api_method = api_method

    async def _request(
            self,
            session: ClientSession,
            data: Dict = None,
            params: Dict = None,
    ) -> ClientResponse:
        async with methodcaller(
            self._http_method,
            f'{TELEGRAM_BOT_API_URL}{self._api_method}',
            data=dumps(data if data else {}),
            params=params if params else {},
            headers={'Content-Type': 'application/json'},
        )(session) as response:
            return response

    def __call__(
            self,
            session: ClientSession,
            data: Dict = None,
            params: Dict = None,
    ):
        return self._request(session, data=data, params=params)

    @classmethod
    def get(cls,  api_method: str):
        return cls('get', api_method)

    @classmethod
    def post(cls,  api_method: str):
        return cls('post', api_method)


telegram_api_get_file_method = _TelegramApiRequestBuilder.get('getFile')
telegram_api_send_message = _TelegramApiRequestBuilder.post('sendMessage')
telegram_api_get_webhookinfo = _TelegramApiRequestBuilder.get('getWebhookinfo')
telegram_api_set_webhook = _TelegramApiRequestBuilder.post('setWebhook')
