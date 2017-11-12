# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse('new user registration page')
    
def login(request):
    return HttpResponse('login form')
    
def new(request):
    return HttpResponse('processes registration form')

def show(request):
    return HttpResponse('list of all the users')

