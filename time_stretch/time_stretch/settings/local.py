# -*- coding: utf-8 -*-
from .common import *


# DEBUG
DEBUG = True
TEMPLATE_DEBUG = DEBUG
# END DEBUG


# Mail settings
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# End mail settings

# django-debug-toolbar
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
# end django-debug-toolbar

# Your local stuff: Below this line define 3rd party libary settings
####### STATIC CONFIGURATION
# STATIC_URL = '/assets/'
# MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
# STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
