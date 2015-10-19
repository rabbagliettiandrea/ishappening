# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
import os
from django.utils.importlib import import_module


STAGE = os.environ.get('ZILLA_STAGE')
local_settings = import_module('ishappening.settings.%s' % STAGE)
globals().update(vars(local_settings))