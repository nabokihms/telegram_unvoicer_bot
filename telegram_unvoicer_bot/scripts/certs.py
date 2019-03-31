import subprocess
from os import getenv


__all__ = [
    'create_certs',
]


def create_certs():
    app_domain = getenv('APP_DOMAIN')
    if app_domain is None:
        print('Environ APP_DOMAIN is not set.')
        return
    
    certificate = getenv('SSL_PATH')
    if certificate is None:
        print('Environ SSL_PATH is not set.')
        return
    
    subprocess.run([
        'openssl', 'req',
        '-newkey', 'rsa:2048',
        '-sha256',
        '-nodes',
        '-keyout', f'{certificate}/private.key',
        '-x509',
        '-days', 365,
        '-out', f'{certificate}/cert.pem',
        '-subj',
        f'/C=US/ST=New York'
        f'/L=Brooklyn'
        f'/O=Unvoicer Company'
        f'/CN={app_domain}',
    ])
