from setuptools import find_packages, setup

_NAME = 'telegram_unvoicer_bot'

setup(
    name=_NAME,
    version='0.0.1',
    description='Бот для Telegram для преобразования голосовых '
                'сообщений в текст.',
    author='Maksim Nabokikh',
    author_email='max.nabokih@gmail.com',
    url='https://github.com/nabokihms/telegram_unvoicer_bot',
    packages=find_packages(exclude=[
        f'{_NAME}.tests*',
    ]),
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'aiohttp==3.2.1',
        'aiofiles==0.3.2',
        'SpeechRecognition==3.8.1',
        'uvloop==0.10.1',
        'gunicorn==19.8.1',
        'Jinja2==2.10',
    ],
    extras_require={
        'dev': [
            'mock>=2.0.0',
            'pytest>=2.3.2'
        ]
    },
    test_suite='tests',
    entry_points={
        'console_scripts': [
            f'{_NAME}_start = {_NAME}.scripts:run',
            f'{_NAME}_create_nginx_conf = {_NAME}.scripts:create_nginx_conf',
            f'{_NAME}_set_webhook = {_NAME}.scripts:set_webhook',
        ]
    }
)
