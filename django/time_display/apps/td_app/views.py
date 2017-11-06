# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime
from time import gmtime, strftime

def index(req):
    # time = datetime.datetime.now()
    time = gmtime()
    print (time)
    context = {
        'time':strftime("%A %B %d, %Y\n%H:%M %p", time)
    }

    return render(req, 'td_app/index.html', context)