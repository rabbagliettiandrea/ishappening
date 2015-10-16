# -*- coding: utf-8 -

from __future__ import unicode_literals, division, absolute_import
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify
from wraith.tentacles.ishappening.models import Document


def index(request, country_slug=None):
    country_id_found = None
    for country_id, country_name in settings.COUNTRY_MAP.iteritems():
        if country_slug == slugify(country_name):
            country_id_found = country_id
            break
    query_kwargs = country_id_found and {'country_id': country_id_found} or {}
    documents = Document.objects.filter(**query_kwargs)[:10]
    d = {
        'documents': documents
    }
    return render(request, 'ishappening/index.html', d)


def serve_document(request, country_slug, internal_url):
    return HttpResponse(Document.objects.get(internal_url=internal_url).html)