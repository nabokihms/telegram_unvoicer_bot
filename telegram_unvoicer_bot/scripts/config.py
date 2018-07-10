import os
import re
from argparse import ArgumentParser
from typing import Dict

import yaml

__all__ = [
    'config2env',
]

_CONFIG_SECTIONS: Dict[str, Dict[str, bool]] = {
    'app': {
        'app_host': False,
        'app_port': False,
        'app_workers': False,
        'app_timeout': False,
        'app_domain': True,
    },
    'telegram_bot': {
        'api_key': True,
    },
    'nginx': {
        'ssl_path': True,
    },
}

_CONFIG_VALIDATORS: Dict[str, str] = {
    # ip адрес
    'app_host': r'((([0-2][0-5][0-5])|((1?)([1-9]?)[0-9]))\.){3}'
                r'(([0-2][0-5][0-5])|((1?)([1-9]?)[0-9]))',
    'app_port': r'[0-9]{1,5}',
    'app_workers': r'[1-9]?[0-9]*',
    'app_timeout': r'[1-9]?[0-9]*',
    'app_domain': r'https?:\/\/(.*)',
    'api_key': r'[0-9]{9}:[0-9A-Za-z_-]{35}',
    'ssl_path': r'(([\w]*|\.{1,2})?/[^/ ]*)+/?',
}


def config2env():
    parser = ArgumentParser()
    parser.add_argument('--config_path', '-c',
                        action='store',
                        help='Путь до файла конфигурации.')

    args = parser.parse_args()
    config_path = args.config_path

    if config_path is None:
        config_path = os.path.join(
            os.getcwd(),
            'settings.yml.example'
        )

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f'Файла конфигурации {config_path} не существует.'
        )

    with open(config_path, 'r') as yamlfile:
        cfg = yaml.load(yamlfile)

        for section, setting in _CONFIG_SECTIONS.items():
            if section not in cfg:
                raise TypeError(
                    f'В конфигурации отсутствует секция {section}.'
                )
            for key in setting:
                if (
                        # Является ли переменная обязательной
                        _CONFIG_SECTIONS[section][key]
                        and key not in cfg[section]
                        and cfg[section][key]
                ):
                    raise TypeError(
                        f'В конфигурации ключ "{key}" в секции "{section}" '
                        f'является обязательным.'
                    )
                value = str(cfg[section].get(key))
                if not value:
                    continue

                validator = re.compile(_CONFIG_VALIDATORS[key])
                if not validator.fullmatch(value):
                    raise TypeError(
                        f'Неверный формат "{key}" в секции "{section}".'
                    )

                os.environ[key.upper()] = str(value)
