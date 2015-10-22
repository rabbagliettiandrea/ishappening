# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from datetime import timedelta
from django.utils.functional import SimpleLazyObject
import os


# ADMINS = [('Andrea', 'rabbagliettiandrea@gmail.com')]
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = 'x5+_bdfc3co*^!5)s-29#rib97pz^bqoxyt3_a^$r8c58@gvd2'
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'ishappening'
]
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware'
]
X_FRAME_OPTIONS = 'DENY'
ROOT_URLCONF = 'ishappening.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'templates')],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_zilla.utils.context_processors.get__settings',
                'django_zilla.utils.context_processors.get__datetime_now',
                'django_zilla.utils.context_processors.get__client_is_logged'
            ],
        },
    },
]
WSGI_APPLICATION = 'wsgi.application'
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'ishappening',
        'USER':     'djangouser',
        'PASSWORD': 'djangouser',
        'HOST':     '127.0.0.1',
        'PORT':     '5432'
    }
}
ATOMIC_REQUESTS = True
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'static')
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
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
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'backend': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}
CACHE_EXPIRE_TIME = timedelta(days=7).total_seconds()
SESSION_COOKIE_AGE = timedelta(weeks=4).total_seconds()
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'session'
REDIS_SERVERS = {
    'default': 'redis://127.0.0.1:6379/0',
    'misc': 'redis://127.0.0.1:6379/1',
    'session': 'redis://127.0.0.1:6379/2',
    'staticfiles': 'redis://127.0.0.1:6379/3',
}
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': CACHE_EXPIRE_TIME,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['default']),
    },
    'misc': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': CACHE_EXPIRE_TIME,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['misc']),
    },
    'session': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': SESSION_COOKIE_AGE,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['session']),
    },
    'staticfiles': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'TIMEOUT': CACHE_EXPIRE_TIME,
        'LOCATION': SimpleLazyObject(lambda: REDIS_SERVERS['staticfiles']),
    }
}
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]
SITE_ID = 1
COUNTRY_MAP = {
    27: 'Italy',
    30: 'Argentina',
    8: 'Australia',
    44: 'Austria',
    41: 'Belgium',
    18: 'Brazil',
    13: 'Canada',
    38: 'Chile',
    32: 'Colombia',
    43: 'Czech Republic',
    49: 'Denmark',
    29: 'Egypt',
    50: 'Finland',
    16: 'France',
    15: 'Germany',
    48: 'Greece',
    10: 'Hong Kong',
    45: 'Hungary',
    3: 'India',
    19: 'Indonesia',
    6: 'Israel',
    4: 'Japan',
    37: 'Kenya',
    34: 'Malaysia',
    21: 'Mexico',
    17: 'Netherlands',
    52: 'Nigeria',
    51: 'Norway',
    25: 'Philippines',
    31: 'Poland',
    47: 'Portugal',
    39: 'Romania',
    14: 'Russia',
    36: 'Saudi Arabia',
    5: 'Singapore',
    40: 'South Africa',
    23: 'South Korea',
    26: 'Spain',
    42: 'Sweden',
    46: 'Switzerland',
    12: 'Taiwan',
    33: 'Thailand',
    24: 'Turkey',
    35: 'Ukraine',
    9: 'United Kingdom',
    1: 'United States',
    28: 'Vietnam'
}