# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.contrib.sitemaps import Sitemap
from ishappening.models import Document


class DocumentsSitemap(Sitemap):
    limit = 1500
    changefreq = "daily"

    def items(self):
        return Document.objects.all().only('timestamp_modified')

    def lastmod(self, obj):
        return obj.timestamp_modified

    def location(self, obj):
        return obj.get_absolute_url()

    def priority(self, obj):
        return 0.5


sitemap_dict = {
    'documents': DocumentsSitemap
}