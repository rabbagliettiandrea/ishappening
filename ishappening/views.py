# -*- coding: utf-8 -

from __future__ import unicode_literals, division, absolute_import
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify
from ishappening.models import Document


def index(request, country_slug=None):
    country_id_found = None
    for country_id, country_name in settings.COUNTRY_MAP.iteritems():
        if country_slug == slugify(country_name):
            country_id_found = country_id
            break
    query_kwargs = country_id_found and {'country_id': country_id_found} or {}
    country_name = settings.COUNTRY_MAP.get(country_id_found, '')
    documents = Document.objects.filter(**query_kwargs)
    top_documents, documents = documents[:4], documents[4:]
    paginator = Paginator(documents, 20)
    try:
        documents = paginator.page(request.GET['page'])
    except (KeyError, PageNotAnInteger):
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)
    d = {
        'top_documents': top_documents,
        'documents': documents,
        'country_name': country_name
    }
    return render(request, 'index.html', d)


def help(request):
    return render(request, 'help.html')


def serve_document(request, country_slug, internal_url):
    return HttpResponse(Document.objects.get(internal_url=internal_url).html)