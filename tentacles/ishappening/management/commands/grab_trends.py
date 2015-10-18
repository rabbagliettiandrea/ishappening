# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division
from django.core.management.base import BaseCommand
from django.db import transaction
from wraith.tentacles.ishappening import spider


class Command(BaseCommand):
    help = 'Grab worldwide Hot Google Trends'

    @transaction.atomic
    def handle(self, *args, **options):
        print 'Documents added: %d' % spider.grab_documents(clear_before=False)