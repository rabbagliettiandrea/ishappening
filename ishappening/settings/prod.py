# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from ishappening.settings._common import *


DEBUG = False
DATABASES['default']['CONN_MAX_AGE'] = 600
for TEMPLATE in TEMPLATES:
    TEMPLATE['OPTIONS']['loaders'] = [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader'
        ])
    ]