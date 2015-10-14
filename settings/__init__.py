# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from krakenv.tentacle import Tentacle


TENTACLES = {
    'andre.ishappening.today': Tentacle(
        path='wraith.tentacles.ishappening', database='ishappening'),
}


APPS = []