# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.conf.urls import url, include
from . import views
from . import admin
from wraith.tentacles.ishappening.sitemap import sitemap_dict


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.grab_documents, name='grab_documents'),
    url(r'^news/(?P<internal_url>.+)$', views.index, name='index'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemap_dict}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemap_dict})
]