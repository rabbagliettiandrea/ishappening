# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.contrib import admin
from ishappening.admin import site as custom_site


def _handle_admin():
    """
    Admin site-wide setup
    """
    admin.site = custom_site


_handle_admin()