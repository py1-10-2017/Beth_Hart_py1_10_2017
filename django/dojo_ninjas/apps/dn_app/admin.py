# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Dojo, Ninja

admin.site.register(Dojo)
admin.site.register(Ninja)
