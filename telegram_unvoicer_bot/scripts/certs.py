import subprocess
from os import getenv


__all__ = [
    'create_certs',
]


def create_certs():
    ssl_path = getenv('SSL_PATH')
    subprocess.run([
        'openssl', 'req',
        '-newkey', 'rsa:2048',
        '-sha256',
        '-nodes',
        '-keyout', f'{ssl_path}/private.key',
        '-x509',
        '-days', 365,
        '-out', f'{ssl_path}/cert.pem',
        '-subj',
        f'/C=US/ST=New York'
        f'/L=Brooklyn'
        f'/O=Unvoicer Company'
        f'/CN={getenv("APP_DOMAIN")}',
    ])
