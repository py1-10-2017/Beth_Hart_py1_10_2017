# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'applogreg/index.html')
    
def register(request):
    #validate collected form data and return errors
    errors = User.objects.regvalidation(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    #encrypt/hash password
    else:
        safe_pw = bcrypt.hashpw(request.POST['password1'].encode(), bcrypt.gensalt())
        new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],password=safe_pw)
    #save registration to DB
        new_user.save()
        messages.success(request, 'You are now registered.')
        request.session['first_name'] = request.POST['first_name']
    return render(request, 'applogreg/success.html')
    
def login(request):
    old_user = User.objects.filter(email=request.POST['email'])
    if old_user:
        password = old_user[0].password
        if bcrypt.checkpw(request.POST['password'].encode(), password.encode()):
            return render(request, 'applogreg/success.html')
        else:
            return redirect('/')
    else:
        messages.error(request, 'email not found')
        return redirect('/')  


