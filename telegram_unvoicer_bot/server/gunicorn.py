import subprocess
from os import cpu_count
from typing import Dict, Any

from telegram_unvoicer_bot.settings import HOST_IP, HOST_PORT

_SETTINGS: Dict[str, Any[str, int]] = {
    '-b': f'{HOST_IP}:{HOST_PORT}',
    '-t': 300,
    '-w': cpu_count(),
    '-k': 'aiohttp.worker.GunicornUVLoopWebWorker',
}


def run_gunicorn_workers():
    subprocess.run([
        'gunicorn',
        *(f'{key} {setting}' for key, setting in _SETTINGS.items()),
        'telegram_unvoicer_bot.server:app'
    ])
