from argparse import ArgumentParser

from telegram_unvoicer_bot.server import run_gunicorn_workers

__all__ = [
    'run',
]


def run():
    parser = ArgumentParser()
    parser.add_argument('--daemon', '-D',
                        nargs='?',
                        default=False,
                        const=True,
                        help='Запустить воркеры в фоновом режиме.')
    parser.add_argument('--reload',
                        nargs='?',
                        default=False,
                        const=True,
                        help='Перезагрузка воркеров при изменении кода.')

    args = parser.parse_args()
    run_gunicorn_workers(daemon=args.daemon, reload=args.reload)


if __name__ == '__main__':
    run()
