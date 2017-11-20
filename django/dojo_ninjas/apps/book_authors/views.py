# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Book, Author
from django.contrib import messages

def index(request):
    books = Book.objects.all()
    context = {'books' : books}
    return render(request, 'book_authors/index.html', context)
    
def new(request):
    if request.method != 'POST':
        return render(request, 'book_authors/new.html')
    else:
        errors = Book.objects.validate_fields(request.POST)
        
        if len(errors)>0:
            for error in errors:
                messages.error(request, error)
            # context ={'messages':messages.error(request,  errors['text'])}
            return render(request, "book_authors/new.html")
        else:
            book=Book(name=request.POST['name'], desc=request.POST['desc'])
            book.save()
            author=Author(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email = request.POST['email'], notes=request.POST['notes'])
            author.save()
            book.authors.add(author)
            return redirect('/')
    
