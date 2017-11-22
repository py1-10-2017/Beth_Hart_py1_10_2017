# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .models import *

def index(request):
    reviews = Review.objects.all()
    books = Book.objects.values('title')
    return render(request, 'books/index.html', {'reviews':reviews[:5], 'books':books})

def new(request):
    return render(request, 'books/new.html')
    
def create(request):
    a = Author(name=request.POST['new_author'])
    a.save()
    b = Book(title=request.POST['title'], author=a)
    b.save()
    r = Review(content=request.POST['content'], rating=request.POST['rating'], book=b)
    r.save()
    return redirect('show/' + str(b.id))
    
def show(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = book.reviews.all()
    context={'book': book, 'reviews': reviews}
    return render(request, 'books/show.html', context)
    

