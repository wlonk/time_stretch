# -*- coding: utf-8 -*-

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
# try:
#     from S3 import CallingFormat
#     AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
# except ImportError:
#     # TODO: Fix this where even if in Dev this class is called.
#     pass

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

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (
        AWS_EXPIREY, AWS_EXPIREY)
}

# # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
# # END STORAGE CONFIGURATION

# Name and email addresses of recipients
ADMINS = (
    ("Ben Warren", "ben@time_stretch.com"),
)

EMAIL_PORT = getenv('MAILGUN_SMTP_PORT')
EMAIL_TIMEOUT = 10
EMAIL_HOST = getenv('MAILGUN_SMTP_SERVER')
EMAIL_HOST_USER = getenv('MAILGUN_SMTP_LOGIN')
EMAIL_HOST_PASSWORD = getenv('MAILGUN_SMTP_PASSWORD')

INVOICE_FROM_EMAIL = "ben@time_stretch.com"

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
