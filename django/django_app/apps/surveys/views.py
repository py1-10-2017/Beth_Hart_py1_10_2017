# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse('List of all surveys')

def new(request):
    return HttpResponse('Form to add a new survey')

