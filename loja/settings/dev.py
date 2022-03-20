import environ

from loja.settings.base import *

env = environ.Env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': env.db()
}


# Django-Summernote
# X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs5'

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEBUG TOOLBAR
INTERNAL_IPS = [
    'localhost',
    '127.0.0.1',
]
