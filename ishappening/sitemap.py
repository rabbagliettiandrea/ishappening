# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.contrib.sitemaps import Sitemap
from django.db.models import Max
from ishappening.models import Document


class DocumentsSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Document.objects.all()

    def lastmod(self, obj):
        return obj.timestamp_modified

    def location(self, obj):
        return obj.get_absolute_url()

    def priority(self, obj):
        return obj.approx_traffic / Document.objects.aggregate(Max('approx_traffic'))['approx_traffic__max']


sitemap_dict = {
    'documents': DocumentsSitemap
}