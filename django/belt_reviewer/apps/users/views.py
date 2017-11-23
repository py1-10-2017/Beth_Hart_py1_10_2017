# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request, 'users/register.html')

def show(request, user_id):
    profile = User.objects.get(id=user_id)
    reviews = profile.reviews.all()
    return render(request, 'users/show.html', {'user':profile, 'reviews': reviews})
    
def register(request):
    errors=User.objects.regvalidation(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
            return redirect('/')
    else:
        password = request.POST['password1']
        safepw= bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        auth_user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],password=safepw)
        print (auth_user)
        request.session['auth']=True
        messages.success(request, 'You are now registered! Welcome, ' + request.POST['first_name'] + '!')
        return redirect('/books')


def login(request):
    return HttpResponse('login')
