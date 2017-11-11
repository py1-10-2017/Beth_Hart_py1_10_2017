# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    return render(request, 'amadon_app.index.html')
    
def buy(request):
    return redirect('/')