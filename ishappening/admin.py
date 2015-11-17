# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.contrib.admin import ModelAdmin, AdminSite
from django_zilla.utils.admin_mixin import LinkOnSiteMixin
from ishappening.models import Document


site = AdminSite()


class DocumentAdmin(LinkOnSiteMixin, ModelAdmin):
    fields = ['title', 'picture_url', 'snippet', 'html', 'approx_traffic', 'country_id', 'published',
              'internal_url', 'external_url']
    list_display = ['title', 'link_on_site']


site.register(Document, DocumentAdmin)