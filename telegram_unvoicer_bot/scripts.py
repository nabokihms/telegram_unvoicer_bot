import os
import os
import sys

import aiohttp
from jinja2 import Template
from telegram_unvoicer_bot.settings import HOST_PORT, HOST_URL, HOST_IP, \
    WEBHOOKS_URL, SSL_CERTIFICATES_PATH

from telegram_unvoicer_bot.server import run_gunicorn_workers
from telegram_unvoicer_bot.telegram import TelegramApiRequest


def run():
    run_gunicorn_workers()


def create_nginx_conf():
    args = sys.argv[1:]
    assert len(args) == 2, \
        'You should specify two arguments. ' \
        'First - template file. Second - path for saving nginx.conf.'

    template_file = args[0]
    assert os.path.isfile(template_file), 'Template does not exist.'

    save_path = args[1]
    assert os.path.isdir(save_path), 'nginx.conf saving path does not exist.'

    with open(template_file) as file_:
        template = Template(file_.read())

    render = template.render(
        host=HOST_IP,
        port=HOST_PORT,
        server_name=HOST_URL,
        webhook_url=WEBHOOKS_URL,
        cert_path=SSL_CERTIFICATES_PATH,
    )

    nginx_config_file = f'{save_path}/nginx.conf'
    with open(nginx_config_file, 'w+') as f:
        f.writelines(render)

    print(f'Nginx config successfully saved in {nginx_config_file}.')


async def _curl():
    async with aiohttp.ClientSession() as session:
        response = await TelegramApiRequest.post(
            'setWebhook', data={
                'url': f'https://{HOST_URL}{WEBHOOKS_URL}',
                'certificate': f'@{SSL_CERTIFICATES_PATH}/cert.pem',
            }
        )(session)
        data = await response.json()
        print(f'Webhook info {data}.')
