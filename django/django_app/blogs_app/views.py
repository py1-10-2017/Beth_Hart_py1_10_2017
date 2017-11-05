# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse('You have reached the Index')


def new(req):
    return HttpResponse('You have reached the New route')


def create(req):
    return HttpResponse('You have reached the create route')


def show(req):
    return HttpResponse('You have reached the show route')


def edit(req):
    return HttpRequest('You have reached the edit route')


def delete(req):
    return HttpRequest('You have reached the destroy route')
