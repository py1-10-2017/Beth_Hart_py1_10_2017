# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    word = get_random_string(length=14)
    context = {'word': word}
    print(dict(request.session))
    return render(request, 'rwg_app/index.html', context)
    
def reset(request):
    try:
        del request.session['attempt']
        
    except:
        print(dict(request.session))
        return redirect ('/')
    print(dict(request.session))
    return redirect('/')

