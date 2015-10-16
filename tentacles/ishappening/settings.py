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
