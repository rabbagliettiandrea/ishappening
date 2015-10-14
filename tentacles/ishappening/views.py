# -*- coding: utf-8 -

from __future__ import unicode_literals, division, absolute_import
from datetime import datetime
from urlparse import urlparse
from bs4 import BeautifulSoup
from django.http import HttpResponse
import feedparser
import requests
import re
import time
from wraith.tentacles.ishappening.models import Document


DELOCALIZE_RESOURCES = re.compile(r'="(/[^/].*?)"')


def index(request):
    Document.objects.all().delete()
    response = requests.get('http://hawttrends.appspot.com/api/terms/')
    hawttrends = response.json()
    data = []
    for country_id in hawttrends.keys()[:1]: # TODO
        response_hottrends = requests.get('https://www.google.com/trends/hottrends/atom/feed?pn=p%s' % country_id)
        serp = feedparser.parse(response_hottrends.content)['entries']
        for result in serp[:1]: # TODO
            html_title = result.get('ht_news_item_title')
            external_url = result.get('ht_news_item_url')
            if not html_title or not external_url:
                continue
            title_soup = BeautifulSoup(html_title)
            title = title_soup.get_text()
            approx_traffic = int(result.get('ht_approx_traffic').replace('+', '').replace(',', ''))
            published = datetime.fromtimestamp(
                time.mktime(result.get('published_parsed')))
            html = unicode(BeautifulSoup(requests.get(external_url).content))
            parsed_uri = urlparse(external_url)
            html_cleaned = DELOCALIZE_RESOURCES.sub(
                r'="%s://%s\g<1>"' % (parsed_uri.scheme, parsed_uri.netloc) , html)
            d = {
                'country_id': country_id,
                'title': title,
                'external_url': external_url,
                'approx_traffic': approx_traffic,
                'published': published
            }
            data.append(d)
            if not Document.objects.filter(external_url=external_url).exists():
                Document.objects.create(
                    title=title,
                    html=html_cleaned,
                    external_url=external_url,
                    country_id=country_id,
                    approx_traffic=approx_traffic,
                    published=published
                )
    return HttpResponse(Document.objects.order_by('?')[0].html)