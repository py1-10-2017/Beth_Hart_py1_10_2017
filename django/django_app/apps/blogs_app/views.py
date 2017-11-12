# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(req):
    return HttpResponse('List of Blogs')


def new(req):
    return HttpResponse('Form to create a blog')


def create(req):
    return redirect("/")


def show(req, blog_id):
    return HttpResponse('Dispaly contents of blog ' + str(blog_id))


def edit(req, blog_id):
    return HttpResponse('Edit blog ' + str(blog_id))


def destroy(req, blog_id):
    return redirect('/')
