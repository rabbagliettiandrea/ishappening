# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from krakenv.tentacle import Tentacle


TENTACLES = {
    'andre.krakenv.io': Tentacle(
        path='wraith.tentacles.default', database='default'),
    'andre.pourich.com': Tentacle(
        path='wraith.tentacles.pourich', database='pourich'),
    'andre.spesafacile.it': Tentacle(
        path='wraith.tentacles.spesafacile', database='spesafacile'),
}


APPS = [
    'wraith.apps.googleads_manager',
    'wraith.apps.magento_manager',
    'wraith.apps.web_crawling',
]