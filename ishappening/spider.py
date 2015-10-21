# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from Queue import Queue
from datetime import datetime
from httplib import HTTPException
from multiprocessing.pool import ThreadPool
from urlparse import urlparse
from bs4 import BeautifulSoup
from django.conf import settings
from django.db import IntegrityError
from django.db.models import Q
import feedparser
import requests
from requests.exceptions import RequestException
import re
import time
from ishappening.models import Document


DELOCALIZE_RESOURCES = re.compile(r'="(/[^/].*?)"')
T_Q = Queue()


def _work(country_id):
    count = 0
    try:
        response_hottrends = requests.get('https://www.google.com/trends/hottrends/atom/feed?pn=p%s' % country_id)
        results = feedparser.parse(response_hottrends.content)['entries']
        for result in results:
            html_title = result.get('ht_news_item_title')
            external_url = result.get('ht_news_item_url')
            if not html_title or not external_url:
                continue
            parsed_uri = urlparse(external_url)
            internal_url = parsed_uri.query and '%s?%s' % (parsed_uri.path.lstrip('/'), parsed_uri.query) \
                           or parsed_uri.path.lstrip('/')
            if Document.objects.filter(
                    Q(internal_url=internal_url) | Q(external_url=external_url)).exists():
                continue
            title_soup = BeautifulSoup(html_title)
            title = title_soup.get_text()
            html_snippet = result.get('ht_news_item_snippet')
            snippet_soup = BeautifulSoup(html_snippet)
            snippet = snippet_soup.get_text()
            approx_traffic = int(result.get('ht_approx_traffic').replace('+', '').replace(',', ''))
            published = datetime.fromtimestamp(
                time.mktime(result.get('published_parsed')))
            picture_url = result.get('ht_picture', '')
            try:
                html = unicode(BeautifulSoup(requests.get(external_url).content))
            except RequestException:
                continue
            html_cleaned = DELOCALIZE_RESOURCES.sub(
                r'="%s://%s\g<1>"' % (parsed_uri.scheme, parsed_uri.netloc) , html)
            try:
                Document.objects.create(
                    title=title,
                    picture_url=picture_url,
                    html=html_cleaned,
                    snippet=snippet,
                    external_url=external_url,
                    internal_url=internal_url,
                    country_id=country_id,
                    approx_traffic=approx_traffic,
                    published=published
                )
            except IntegrityError:
                continue
            count += 1
    except (RequestException, HTTPException):
        pass
    T_Q.put(count)


def grab_documents(clear_before):
    clear_before and Document.objects.all().delete()
    pool = ThreadPool(processes=len(settings.COUNTRY_MAP))
    pool.map(_work, settings.COUNTRY_MAP.iterkeys())
    pool.close()
    pool.join()
    return sum(T_Q.queue)
