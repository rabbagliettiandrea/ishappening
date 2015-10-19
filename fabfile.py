# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from fabric.contrib import django as fab_django

fab_django.settings_module('ishappening.settings')

from django_zilla.fabric_tasks import select, misc, srv, git, db, migrations