from typing import FrozenSet, Dict

from telegram_unvoicer_bot.settings import TELEGRAM_BOT_API_KEY

TELEGRAM_BOT_API_URL_PREFIX: str = 'https://api.telegram.org'
TELEGRAM_BOT_API_URL: str = \
    f'{TELEGRAM_BOT_API_URL_PREFIX}/bot{TELEGRAM_BOT_API_KEY}/'
TELEGRAM_BOT_FILE_PATH_API_URL: str = \
    f'{TELEGRAM_BOT_API_URL_PREFIX}/file/bot{TELEGRAM_BOT_API_KEY}/'

TELEGRAM_MESSAGE_AUDIO_KEYS: FrozenSet[str] = frozenset(
    ('voice', 'audio', 'document')
)

TELEGRAM_REQUEST_HEADERS: Dict[str, str] = {'Content-Type': 'application/json'}
TELEGRAM_REQUEST_ALLOWED_HTTP_METHODS: FrozenSet[str] = frozenset(
    ('get', 'post')
)
TELEGRAM_REQUEST_ALLOWED_API_METHODS: FrozenSet[str] = frozenset(
    ('getFile', 'sendMessage', 'getWebhookinfo', 'setWebhook')
)
