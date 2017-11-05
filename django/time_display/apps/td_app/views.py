# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime
from pytz import timezone
import time

def index(req):
    time = datetime.datetime.now()

    context = {
        'time':time
    }

    return render(req, 'td_app/index.html', context)