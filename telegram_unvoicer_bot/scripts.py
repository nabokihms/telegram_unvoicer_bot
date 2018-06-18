import os
import sys

from jinja2 import Template
from telegram_unvoicer_bot.settings import HOST_PORT, HOST_URL, HOST_IP, \
    WEBHOOKS_URL, SSL_CERTIFICATES_PATH

from telegram_unvoicer_bot.server import run_gunicorn_workers


def run():
    run_gunicorn_workers()


def create_nginx_conf():
    args = sys.argv[1:]
    assert len(args) == 2, \
        'Необходимо указать два аргумента. ' \
        'Первый - путь до шаблона. Второй - путь для сохранения nginx.conf.'

    template_file = args[0]
    assert os.path.isfile(template_file), 'Шаблон не существует.'

    save_path = args[1]
    assert os.path.isdir(save_path), 'Путь для сохранения nginx.conf не ' \
                                     'существует.'

    with open(template_file) as file_:
        template = Template(file_.read())

    render = template.render(
        host=HOST_IP,
        port=HOST_PORT,
        server_name=HOST_URL,
        webhook_url=WEBHOOKS_URL,
        cert_path=SSL_CERTIFICATES_PATH,
    )

    nginx_config_file: str = f'{save_path}/nginx.conf'
    with open(nginx_config_file, 'w+') as f:
        f.writelines(render)

    print(f'Конфигурация nginx успешно сохранена в {nginx_config_file}.')
