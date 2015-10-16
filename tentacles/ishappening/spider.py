# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from Queue import Queue
from datetime import datetime
from multiprocessing.pool import ThreadPool
from urlparse import urlparse
from bs4 import BeautifulSoup
import feedparser
import requests
from requests.exceptions import RequestException
import re
import time
from wraith.tentacles.ishappening.models import Document


DELOCALIZE_RESOURCES = re.compile(r'="(/[^/].*?)"')


def _work(t):
    q = t[0]
    country_id = t[1]
    try:
        response_hottrends = requests.get('https://www.google.com/trends/hottrends/atom/feed?pn=p%s' % country_id)
        serp = feedparser.parse(response_hottrends.content)['entries']
        for result in serp[:5]:
            html_title = result.get('ht_news_item_title')
            external_url = result.get('ht_news_item_url')
            if not html_title or not external_url or \
                    Document.objects.using('ishappening').filter(external_url=external_url).exists():
                continue
            parsed_uri = urlparse(external_url)
            internal_url = parsed_uri.query and '%s?%s' % (parsed_uri.path.lstrip('/'), parsed_uri.query) \
                           or parsed_uri.path.lstrip('/')
            title_soup = BeautifulSoup(html_title)
            title = title_soup.get_text()
            html_snippet = result.get('ht_news_item_snippet')
            snippet_soup = BeautifulSoup(html_snippet)
            snippet = snippet_soup.get_text()
            approx_traffic = int(result.get('ht_approx_traffic').replace('+', '').replace(',', ''))
            published = datetime.fromtimestamp(
                time.mktime(result.get('published_parsed')))
            picture_url = result.get('ht_picture', '')
            html = unicode(BeautifulSoup(requests.get(external_url).content))
            html_cleaned = DELOCALIZE_RESOURCES.sub(
                r'="%s://%s\g<1>"' % (parsed_uri.scheme, parsed_uri.netloc) , html)
            q.put({
                'title': title,
                'picture_url': picture_url,
                'external_url': external_url,
                'internal_url': internal_url,
                'country_id': country_id,
                'approx_traffic': approx_traffic,
                'published': unicode(published)
            })
            if not Document.objects.using('ishappening').filter(external_url=external_url).exists():
                Document.objects.using('ishappening').create(
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
    except RequestException:
        pass


def grab_documents(clear_before):
    if clear_before:
        Document.objects.using('ishappening').delete()
    response = requests.get('http://hawttrends.appspot.com/api/terms/')
    hawttrends = response.json()
    q = Queue()
    pool = ThreadPool(processes=len(hawttrends))
    pool.map(_work, ((q, hawttrend) for hawttrend in hawttrends))
    pool.close()
    pool.join()
    data = []
    for d in iter(q.queue):
        data.append(d)
    return data