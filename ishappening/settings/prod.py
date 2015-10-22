# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from ishappening.settings._common import *


# DEBUG = True
DATABASES['default']['CONN_MAX_AGE'] = 600
# for TEMPLATE in TEMPLATES:
#     TEMPLATE['options']['loaders'] = \
#         ('django.template.loaders.cached.Loader', [
#             'django.template.loaders.filesystem.Loader',
#             'django.template.loaders.app_directories.Loader'
#         ])