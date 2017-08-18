import os

import django_cache_url
import dj_database_url
import raven

from .base import *  # noqa

# Do not set SECRET_KEY, Postgres or LDAP password or any other sensitive data here.
# Instead, use environment variables or create a local.py file on the server.

# Disable debug mode
DEBUG = False

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# enable HSTS only once the site is working properly on https with the actual live domain name
# SECURE_HSTS_SECONDS = 31536000  # 1 year


# Cache everything for 10 minutes
# This only applies to pages that do not have a more specific cache-control
# setting. See urls.py
CACHE_CONTROL_MAX_AGE = 600


# Google tag manager

GOOGLE_TAG_MANAGER_ID = 'GTM-K8CGDX6'


# Newsletter

NEWSLETTER_URL = '//nhs.us8.list-manage.com/subscribe?u=04af4dde330becaf38e8eb355&id=1a71ed9a1e'


# Configuration from environment variables
# Alternatively, you can set these in a local.py file on the server

env = os.environ.copy()

# CFG_ prefixed environment variables are made available for use by the application
for key, value in os.environ.items():
    if key.startswith('CFG_'):
        env[key[4:]] = value


# Basic configuration

APP_NAME = env.get('APP_NAME', 'hra')

if 'SECRET_KEY' in env:
    SECRET_KEY = env['SECRET_KEY']

if 'ALLOWED_HOSTS' in env:
    ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')

if 'PRIMARY_HOST' in env:
    BASE_URL = 'http://%s/' % env['PRIMARY_HOST']

if 'SERVER_EMAIL' in env:
    SERVER_EMAIL = env['SERVER_EMAIL']
    DEFAULT_FROM_EMAIL = env['SERVER_EMAIL']

if 'EMAIL_SUBJECT_PREFIX' in env:
    EMAIL_SUBJECT_PREFIX = env['EMAIL_SUBJECT_PREFIX']

if 'CACHE_PURGE_URL' in env:
    INSTALLED_APPS += ('wagtail.contrib.wagtailfrontendcache', )  # noqa
    WAGTAILFRONTENDCACHE = {
        'default': {
            'BACKEND': 'wagtail.contrib.wagtailfrontendcache.backends.HTTPBackend',
            'LOCATION': env['CACHE_PURGE_URL'],
        },
    }

if 'STATIC_URL' in env:
    STATIC_URL = env['STATIC_URL']

if 'STATIC_DIR' in env:
    STATIC_ROOT = env['STATIC_DIR']

if 'MEDIA_URL' in env:
    MEDIA_URL = env['MEDIA_URL']

if 'MEDIA_DIR' in env:
    MEDIA_ROOT = env['MEDIA_DIR']


if 'MEDIA_BUCKET' in env:
    AWS_LOCATION ='media/'
    AWS_STORAGE_BUCKET_NAME = env['MEDIA_BUCKET']
    AWS_S3_CUSTOM_DOMAIN = env['AWS_S3_CUSTOM_DOMAIN']
    AWS_S3_URL_PROTOCOL= 'http:' # TODO
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# Database

if 'DATABASE_URL' in os.environ:
    DATABASES = {'default': dj_database_url.config()}

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env.get('PGDATABASE', APP_NAME),
            'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for

            # User, host and port can be configured by the PGUSER, PGHOST and
            # PGPORT environment variables (these get picked up by libpq).
        }
    }


# Redis

if 'CACHE_URL' in os.environ:
    CACHES = {'default': django_cache_url.config()}


# Celery
# Ask sysadmin to add `CFG_BROKER_URL` env var, if you need celery.

if 'BROKER_URL' in env:
    BROKER_URL = env['BROKER_URL']


# Elasticsearch

if 'ELASTICSEARCH_URL' in env:
    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch',
            'URLS': [env['ELASTICSEARCH_URL']],
            'INDEX': APP_NAME,
            'ATOMIC_REBUILD': True,
        },
    }


if 'LOG_DIR' in env:
    # Health Research Authority log
    LOGGING['handlers']['hra_file'] = {
        'level': 'INFO',
        'class': 'cloghandler.ConcurrentRotatingFileHandler',
        'formatter': 'verbose',
        'filename': os.path.join(env['LOG_DIR'], 'hra.log'),
        'maxBytes': 5242880,  # 5MB
        'backupCount': 5
    }
    LOGGING['loggers']['hra']['handlers'].append('hra_file')
    LOGGING['loggers']['hra.research_summaries']['handlers'].append('hra_file')

    # Wagtail log
    LOGGING['handlers']['wagtail_file'] = {
        'level': 'INFO',
        'class': 'cloghandler.ConcurrentRotatingFileHandler',
        'formatter': 'verbose',
        'filename': os.path.join(env['LOG_DIR'], 'wagtail.log'),
        'maxBytes': 5242880,  # 5MB
        'backupCount': 5
    }
    LOGGING['loggers']['wagtail']['handlers'].append('wagtail_file')

    # Error log
    LOGGING['handlers']['errors_file'] = {
        'level': 'ERROR',
        'class': 'cloghandler.ConcurrentRotatingFileHandler',
        'formatter': 'verbose',
        'filename': os.path.join(env['LOG_DIR'], 'error.log'),
        'maxBytes': 5242880,  # 5MB
        'backupCount': 5
    }
    LOGGING['loggers']['django.request']['handlers'].append('errors_file')
    LOGGING['loggers']['django.security']['handlers'].append('errors_file')


# Raven (sentry) configuration.
if 'RAVEN_DSN' in env:
    RAVEN_CONFIG = {
        'dsn': env['RAVEN_DSN'],
        'release': raven.fetch_git_sha(BASE_DIR),
    }


try:
    from .local import *  # noqa
except ImportError:
    pass
