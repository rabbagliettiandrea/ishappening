# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.core.urlresolvers import reverse
from django.db.models import TextField, PositiveIntegerField, DateTimeField, URLField
from django.utils.text import slugify
from django_zilla.utils.models_abstract import TimedatedModel
from ishappening import settings


class Document(TimedatedModel):
    title = TextField()
    picture_url = URLField(blank=True, max_length=600)
    html = TextField()
    snippet = TextField()
    approx_traffic = PositiveIntegerField()
    country_id = PositiveIntegerField(db_index=True)
    published = DateTimeField()
    internal_url = URLField(db_index=True, unique=True, max_length=600)
    external_url = URLField(db_index=True, unique=True, max_length=600)

    class Meta:
        ordering = ['-published']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'serve_document', args=[slugify(settings.COUNTRY_MAP[self.country_id]), self.internal_url])