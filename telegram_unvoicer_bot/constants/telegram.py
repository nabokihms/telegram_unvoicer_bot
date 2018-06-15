from telegram_unvoicer_bot.settings import TELEGRAM_BOT_API_KEY

TELEGRAM_BOT_API_URL_PREFIX = 'https://api.telegram.org'
TELEGRAM_BOT_API_URL = \
    f'{TELEGRAM_BOT_API_URL_PREFIX}/bot{TELEGRAM_BOT_API_KEY}/'
TELEGRAM_BOT_FILE_PATH_API_URL = \
    f'{TELEGRAM_BOT_API_URL_PREFIX}/file/bot{TELEGRAM_BOT_API_KEY}/'

TELEGRAM_MESSAGE_AUDIO_KEYS = frozenset(('voice', 'audio', 'document'))

TELEGRAM_REQUEST_HEADERS = {'Content-Type': 'application/json'}
TELEGRAM_REQUEST_ALLOWED_HTTP_METHODS = frozenset(('get', 'post'))
TELEGRAM_REQUEST_ALLOWED_API_METHODS = frozenset(
    ('getFile', 'sendMessage', 'getWebhookinfo', 'setWebhook')
)
