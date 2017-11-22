# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'users/register.html')

def show(request, user_id):
    return HttpResponse('show page')
