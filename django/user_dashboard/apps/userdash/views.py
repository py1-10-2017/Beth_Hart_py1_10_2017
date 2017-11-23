# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'userdash/index.html')
    
def login(request):
    return render(request, 'userdash/login.html')
    
def register(request):
    return render(request, 'userdash/register.html')
    
