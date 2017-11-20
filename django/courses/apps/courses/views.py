# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course, Description


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses':courses} )
    
def create(request):
    Course.objects.create(name=request.POST['name'], description=Description(text=request.POST['desc']))
    return redirect('/')
    
def warning(request, course_id):
    course = Course.objects.filter(id=course_id).all()
    print(course)
    return render(request, 'courses/destroy.html', {'course': course})
    
def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
