# -*- coding: utf-8 -*-
"""views for users app"""
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import User
from django.contrib import messages
def index(request):
    users = User.objects.all()
    
    return render(request, 'users/index.html', {'users': users})

def new(request):
    return render(request, 'users/new.html')
    
def create(request):
    #run validation
    errors = User.objects.validate_fields(request.POST)
    print(errors)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        print (messages)
        return render(request, 'users/new.html')
    else:
        new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        new_user.save()
        return redirect(reverse('users:index'))

def edit(request):
    pass
def show(request):
    pass

def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect(reverse('users:index'))