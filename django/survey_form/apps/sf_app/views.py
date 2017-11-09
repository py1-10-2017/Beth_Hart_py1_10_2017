# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(req):
    return render(req, 'sf_app/index.html')
    
def result(req):
    print(dict(req.session))
    return render(req, 'sf_app/result.html')
    
def process(req):
    if req.method == 'POST':
        req.session['form'] = req.POST
        
        print (req.POST)
    return redirect ('/result')
