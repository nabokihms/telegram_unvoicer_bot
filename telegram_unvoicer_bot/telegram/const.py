from os import getenv
from typing import FrozenSet


TELEGRAM_BOT_API_KEY = getenv('API_KEY', '')

TELEGRAM_BOT_API_URL_PREFIX: str = 'https://api.telegram.org'
TELEGRAM_BOT_API_URL: str = \
    f'{TELEGRAM_BOT_API_URL_PREFIX}/bot{TELEGRAM_BOT_API_KEY}/'
TELEGRAM_BOT_FILE_PATH_API_URL: str = \
    f'{TELEGRAM_BOT_API_URL_PREFIX}/file/bot{TELEGRAM_BOT_API_KEY}/'

TELEGRAM_MESSAGE_AUDIO_KEYS: FrozenSet[str] = frozenset(
    ('voice', 'audio', 'document')
)

