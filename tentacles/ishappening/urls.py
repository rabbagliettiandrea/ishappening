# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.conf.urls import url, include
from . import views
from . import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
]