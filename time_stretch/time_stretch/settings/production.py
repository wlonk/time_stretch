# -*- coding: utf-8 -*-

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
try:
    from S3 import CallingFormat
    AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
except ImportError:
    # TODO: Fix this where even if in Dev this class is called.
    pass

from .common import *

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# django-secure
INSTALLED_APPS += ("djangosecure", )

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = True
# end django-secure

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
# END SITE CONFIGURATION

INSTALLED_APPS += ("gunicorn", )

# STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'storages',
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

# see: https://github.com/antonagestam/collectfast
AWS_PRELOAD_METADATA = True
INSTALLED_APPS += ("collectfast", )

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (
        AWS_EXPIREY, AWS_EXPIREY)
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
# END STORAGE CONFIGURATION

# EMAIL
# DEFAULT_FROM_EMAIL = 'time_stretch <noreply@example.com>'
# EMAIL_HOST = 'smtp.sendgrid.com')
# EMAIL_HOST_PASSWORD = environ_prefix="", environ_name="SENDGRID_PASSWORD"
# EMAIL_HOST_USER = environ_prefix="", environ_name="SENDGRID_USERNAME"
# EMAIL_PORT = 587, environ_prefix="", environ_name="EMAIL_PORT"
# EMAIL_SUBJECT_PREFIX = '[time_stretch] ', environ_name="EMAIL_SUBJECT_PREFIX"
# EMAIL_USE_TLS = True
# SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL

# TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
# END TEMPLATE CONFIGURATION

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION

# Your production stuff: Below this line define 3rd party libary settings
