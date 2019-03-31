from asyncio import AbstractEventLoop
from operator import contains
from typing import Optional, Tuple

from aiohttp import ClientSession, web, ClientRequest

from .abc import AbstractTelegramHandler
from .audio_handler import AudioTelegramSupportHandler
from .const import TELEGRAM_MESSAGE_AUDIO_KEYS


class TelegramWebhookHandler(AbstractTelegramHandler):
    """
    Основной обработчик вебхуков от телеграма.
    """
    # todo: проработать систему логирования.
    def __init__(self, loop: AbstractEventLoop):
        self._loop = loop
        self._request = None
        self._data = None

    async def _parse_request(self):
        self._data = await self._request.json()

    @property
    def _command(self) -> Optional[Tuple]:
        """
        Получение команды из строки.
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
        return self._data['message']['chat']['id']

    @property
    def _audio_file_type(self) -> Optional[str]:
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

    async def handle(
            self, request: ClientRequest, *args, **kwargs
    ) -> web.Response:
        """
        Основной метод для обработки вебхуков.
        """
        self._request = request
        await self._parse_request()

        if self._audio_file_type is not None:
            status_code = await self._handle_audio()
            return web.Response(status=status_code)

        return web.Response(status=200)
