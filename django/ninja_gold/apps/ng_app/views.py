# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random, math
from time import strftime, gmtime

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'messages' not in request.session:
        request.session['messages'] = []
    return render(request, 'ng_app/index.html')
    
def process_money(request):
    if request.POST['location'] == 'farm':
        amount = math.floor(random.random()*10) + 10 
        request.session['gold'] += amount   
    elif request.POST['location'] == 'cave':
        amount = math.floor(random.random()*5) + 5  
        request.session['gold'] += amount
    elif request.POST['location'] == 'house':
        amount = math.floor(random.random()*3) + 2 
        request.session['gold'] += amount   
    elif request.POST['location'] == 'casino':
        num = random.random()
        if num < .5:
            amount = math.floor(random.random()*50)
            request.session['gold'] += amount
        else:
            amount = math.floor(random.random()*50)
            request.session['gold'] -= amount
    if request.POST['location'] == 'casino' and num >= .5:
        message = "Oh no! You just lost " + str(amount) + ' golds in the Casino! Rough! ' + strftime("%m/%d/%y, %I:%M", gmtime())
    else:
        message = "Earned " + str(amount) +" gold in the " + request.POST['location'] +" " + strftime("%m/%d/%y, %I:%M", gmtime())
    messages = request.session['messages']
    messages.append(message)
    request.session['messages'] = messages
    return redirect ('/')
    
def clear(request):
    del request.session['gold']
    del request.session['messages']
    return redirect('/')
    
