from asyncio import SelectorEventLoop
from operator import contains

from aiohttp import ClientSession, web

from .abc import AbstractTelegramHandler
from .audio_handler import AudioTelegramSupportHandler
from ..constants import TELEGRAM_MESSAGE_AUDIO_KEYS


class TelegramWebhookHandler(AbstractTelegramHandler):

    # todo: add logging system
    def __init__(self, loop: SelectorEventLoop):
        self._loop = loop
        self._request = None
        self._data = None

    async def _parse_request(self):
        """
        Get json data from request.
        """
        self._data = await self._request.json()

    @property
    def _command(self) -> tuple or None:
        """
        Check if there is a command in message.
        """
        message = self._data['message']
        if 'text' not in message:
            return
        text = message['text']
        if not text.startswith('/'):
            return
        return text[1:].split(' ', maxsplit=1)

    @property
    def _chat_id(self) -> str:
        """
        Get telegram user chat id.
        """
        return self._data['message']['chat']['id']

    @property
    def _audio_file_type(self) -> str or None:
        """
        Get audio file information key.
        """
        message = self._data['message']
        types = tuple(filter(
            lambda x: contains(message, x), TELEGRAM_MESSAGE_AUDIO_KEYS
        ))
        if not types:
            return
        return types[0]

    async def _handle_audio(self) -> int:
        async with ClientSession(loop=self._loop) as session:
            return await AudioTelegramSupportHandler(
                session,
                self._chat_id,
                self._data['message'][self._audio_file_type]['file_id']
            ).handle()

    async def handle(self, request, *args, **kwargs) -> web.Response:
        """
        Main method for handling webhooks.
        """
        self._request = request
        await self._parse_request()

        if self._audio_file_type is not None:
            status_code = await self._handle_audio()
            return web.Response(status=status_code)

        return web.Response(status=200)
