# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from krakenv.settings import *


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
RSA_FILEPATH = r'~\.ssh\id_rsa'