from abc import ABC, abstractmethod

from aiohttp import ClientSession

__all__ = [
    'AbstractTelegramHandler',
    'AbstractTelegramSupportHandler',
]


class AbstractTelegramHandler(ABC):
    @abstractmethod
    def handle(self, *args, **kwargs):
        pass


class AbstractTelegramSupportHandler(AbstractTelegramHandler):
    def __init__(self, session: ClientSession, chat_id: str):
        self._session = session
        self._chat_id = chat_id

    @abstractmethod
    def handle(self, *args, **kwargs):
        pass
