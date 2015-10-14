# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from krakenv.admin import AdminSite
from wraith.tentacles.ishappening.models import Document


site = AdminSite()

site.register_from_default_site()
site.register(Document)