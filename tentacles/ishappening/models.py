# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.core.urlresolvers import reverse
from django.db.models import TextField, PositiveIntegerField, DateTimeField, URLField
from django_zilla.utils.models_abstract import TimedatedModel


class Document(TimedatedModel):
    title = TextField()
    html = TextField()
    approx_traffic = PositiveIntegerField()
    country_id = PositiveIntegerField(db_index=True)
    published = DateTimeField()
    internal_url = URLField(db_index=True, unique=True)
    external_url = URLField(db_index=True, unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index', args=[self.internal_url])