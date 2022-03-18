from django.conf import settings

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEBUG TOOLBAR
INTERNAL_IPS = [
    'localhost',
    '127.0.0.1',
]
