# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from krakenv.settings import *


DATABASES['ishappening'] = {
    'ENGINE':   'django.db.backends.postgresql_psycopg2',
    'NAME':     'krakenv__ishappening',
    'USER':     'djangouser',
    'PASSWORD': 'djangouser',
    'HOST':     '127.0.0.1',
    'PORT':     '5432'
}