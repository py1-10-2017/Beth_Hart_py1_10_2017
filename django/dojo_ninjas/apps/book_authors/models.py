'''models for book_authors app'''

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class BookManager(models.Manager):
    def  validate_fields(self, data):
        errors = []
        if len(data['name']) < 5:
            errors.append('name must be 5 characters')
            print(errors)
        return errors

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email= models.EmailField()
    notes= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author, related_name='books')
    objects = BookManager()
    
    def __str__(self):
        return self.name
        

    
