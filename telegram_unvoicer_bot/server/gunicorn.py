import subprocess
from os import cpu_count, getenv


_DEFAULT_SETTINGS = {
    'APP_HOST': '0.0.0.0',
    'APP_PORT': 8080,
    'APP_WORKERS': cpu_count(),
    'APP_TIMEOUT': 300
}


def run_gunicorn_workers(daemon=False, reload=False):
    settings = {
        k: getenv(k) or v
        for k, v in _DEFAULT_SETTINGS.items()
    }
    command = [
        'gunicorn',
        '-b', f'{settings["APP_HOST"]}:{settings["APP_PORT"]}',
        '-w', f'{settings["APP_WORKERS"]}',
        '-t', f'{settings["APP_TIMEOUT"]}',
        '-k', 'aiohttp.worker.GunicornUVLoopWebWorker',
        'telegram_unvoicer_bot.server:app'
    ]

    if reload:
        command.insert(1, '-reload')

    if daemon:
        command.insert(1, '-D')

    subprocess.run(command)
