from setuptools import find_packages, setup

_NAME = 'telegram_unvoicer_bot'

setup(
    name=_NAME,
    version='0.1.0',
    description='Telegram Bot to decoding voicemails into text',
    author='Maksim Nabokikh',
    author_email='max.nabokih@gmail.com',
    url='https://github.com/nabokihms/telegram_unvoicer_bot',
    packages=find_packages(exclude=[
        f'{_NAME}.tests*',
    ]),
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'aiohttp==3.7.3',
        'aiofiles==0.3.2',
        'SpeechRecognition==3.8.1',
        'gunicorn==19.8.1',
        'PyYAML==5.1',
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
            f'{_NAME}_bind_webhook = {_NAME}.scripts:bind_webhook',
            f'{_NAME}_get_webhook_info = {_NAME}.scripts:get_webhook_info',
            f'{_NAME}_generate_certs = {_NAME}.scripts:create_certs',
        ]
    }
)
