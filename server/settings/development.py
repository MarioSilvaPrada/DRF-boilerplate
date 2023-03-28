import socket
from datetime import timedelta
from .base import *

DEBUG = True

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(hours=2)