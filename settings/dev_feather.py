# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from krakenv.settings import *


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
RSA_FILEPATH = r'~\.ssh\id_rsa'
REDIS_SERVERS['magento_pourich'] = 'redis://192.168.30.233:6379/0'
REDIS_SERVERS['magento_spesafacile'] = 'redis://192.168.30.233:6379/1'