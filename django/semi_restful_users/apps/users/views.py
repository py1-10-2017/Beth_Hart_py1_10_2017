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
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        print (messages)
        return redirect('/users/new')
    else:
        new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        new_user.save()
        return redirect(reverse('users:index'))

def edit(request, user_id):
    edit_user = User.objects.get(id=user_id)
    context = {'user' : edit_user}
    return render(request, 'users/edit.html', context)
   
def update(request, user_id):
    errors = User.objects.validate_fields(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        print (messages)
        return redirect('/users/'+user_id +'/edit')
    else:
        User.objects.filter(id=user_id).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/users')    

def show(request, user_id):
    show_user = User.objects.get(id=user_id)
    return render(request, 'users/show.html', {'user': show_user})

def destroy(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect(reverse('users:index'))