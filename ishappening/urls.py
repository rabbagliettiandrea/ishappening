# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.conf.urls import url, include
from django.views.generic import TemplateView
from ishappening import views, admin
from ishappening.sitemap import sitemap_dict


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^help/$', views.help, name='help'),
    url(r'^$', views.index, name='index_generic'),
    url(r'^(?P<country_slug>[\w-]+)/$', views.index, name='index_country'),
    url(r'^(?P<country_slug>[\w-]+)/(?P<internal_url>.+)/$', views.serve_document, name='serve_document'),
    # Sitemap
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemap_dict}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemap_dict}),
    # robots.txt
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'))
]