# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from operator import itemgetter
from django import template
from django.conf import settings


register = template.Library()


@register.assignment_tag
def get_countries():
    return sorted(settings.COUNTRY_MAP.iteritems(), key=itemgetter(1))
