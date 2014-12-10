# -*- coding: utf-8 -*-
"""
Django settings for time_stretch project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from os import getenv

BASE_DIR = dirname(dirname(dirname(__file__)))


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath,
# this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION

# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'storages',  # serve rom s3 in production
    'pipeline',  # merge all the statics
)

# Apps specific for this project go here.
LOCAL_APPS = (
    # Your stuff: custom apps go here
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# END MIDDLEWARE CONFIGURATION

# MIGRATIONS CONFIGURATION
MIGRATION_MODULES = {
    'sites': 'contrib.sites.migrations'
}
# END MIGRATIONS CONFIGURATION

# DEBUG
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
#       In production, this is changed to a values.SecretValue() setting
SECRET_KEY = getenv('SECRET_KEY')
# END SECRET CONFIGURATION

# FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    join(BASE_DIR, 'fixtures'),
)
# END FIXTURE CONFIGURATION

# EMAIL CONFIGURATION
EMAIL_BACKEND = ('django.core.mail.backends.smtp.EmailBackend')
# END EMAIL CONFIGURATION

# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Ben""", 'bwarren2@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Database settings for Heroku
DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    default="postgres://localhost/time_stretch"
)
########## END DATABASE CONFIGURATION

# CACHING
# Do this here because thanks to django-pylibmc-sasl and pylibmc
# memcacheify (used on heroku) is painful to install on windows.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
# END CACHING

# GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Los_Angeles'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# END GENERAL CONFIGURATION

# TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    # Your stuff: custom template context processers go here
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

####STORAGES####
AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME', '')
DEFAULT_FILE_STORAGE = 'time_stretch.s3utils.MediaRootS3BotoStorage'
AWS_QUERYSTRING_AUTH = False
S3_URL = '//%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_DIRECTORY = '/assets/'
MEDIA_DIRECTORY = '/media/'
# END STORAGES


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = S3_URL + MEDIA_DIRECTORY
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = S3_URL + STATIC_DIRECTORY

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
#      #std:setting-STATICFILES_DIRS
# Note: There is a presumption that the first entry here is 'static' so that
# trash dirs work.
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
#      #staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
     'pipeline.finders.PipelineFinder',
)

STATICFILES_STORAGE = 'time_stretch.s3utils.S3PipelineStorage'

########## END STATIC FILE CONFIGURATION

# URL Configuration
ROOT_URLCONF = 'urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
# End URL Configuration

# AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
# END SLUGLIFIER


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION

# Your common stuff: Below this line define 3rd party library settings

########## PIPELINE CONFIGURATION
            # 'css/override_variables.less',
PIPELINE_CSS = {
    'all': {
        'source_filenames': (
            'css/custom_bootstrap_compilation.less',
            'css/project.less'
        ),
        'output_filename': 'css/all.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'all': {
        'source_filenames': (
            'bootstrap/js/transition.js',
            'bootstrap/js/modal.js',
            'bootstrap/js/dropdown.js',
            'bootstrap/js/scrollspy.js',
            'bootstrap/js/tab.js',
            'bootstrap/js/tooltip.js',
            'bootstrap/js/popover.js',
            'bootstrap/js/alert.js',
            'bootstrap/js/button.js',
            'bootstrap/js/collapse.js',
            'bootstrap/js/carousel.js',
            'bootstrap/js/affix.js',
            'js/project.js',
        ),
        'output_filename': 'js/all.js',
    },
    'jquery': {
        'source_filenames': (
            'js/jquery-1.10.2.js',
        ),
        'output_filename': 'js/jq.js',
    }

}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)
########## END PIPELINE CONFIGURATION
