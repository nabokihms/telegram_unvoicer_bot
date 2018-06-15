from json import dumps
from operator import methodcaller

from aiohttp import ClientResponse, ClientSession

from ..constants import TELEGRAM_BOT_API_URL, TELEGRAM_REQUEST_HEADERS, \
    TELEGRAM_REQUEST_ALLOWED_HTTP_METHODS, TELEGRAM_REQUEST_ALLOWED_API_METHODS


class TelegramApiRequest(object):
    """
    Class for creating and sending requests to telegram api.
    """
    def __init__(
            self,
            http_method: str,
            api_method: str,
            data=None,
            params=None,
    ):
        lowered_http_method = http_method.lower()

        assert lowered_http_method in TELEGRAM_REQUEST_ALLOWED_HTTP_METHODS, \
            f'http method not allowed  - {lowered_http_method}.'
        assert api_method in TELEGRAM_REQUEST_ALLOWED_API_METHODS, \
            f'telegram api method not allowed  - {api_method}.'

        self._http_method = lowered_http_method
        self._api_method = api_method
        self._data = data or {}
        self._params = params or {}

    async def _request(self, session: ClientSession) -> ClientResponse:
        async with methodcaller(
            self._http_method,
            f'{TELEGRAM_BOT_API_URL}{self._api_method}',
            data=dumps(self._data),
            params=self._params,
            headers=TELEGRAM_REQUEST_HEADERS,
        )(session) as response:
            return response

    def __call__(self, session: ClientSession):
        return self._request(session)

    @classmethod
    def get(cls,  api_method: str, data=None, params=None):
        return cls('get', api_method, data, params)

    @classmethod
    def post(cls,  api_method: str, data=None, params=None):
        return cls('post', api_method, data, params)
