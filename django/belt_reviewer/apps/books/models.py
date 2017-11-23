# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import User

class Author(models.Model):
    name= models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author=models.OneToOneField(Author)
    
    def __str__(self):
        return self.title
       
class Review(models.Model):
    content= models.TextField()
    rating=models.IntegerField()
    book=models.ForeignKey(Book, related_name='reviews')
    user=models.ForeignKey(User, related_name='reviews')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.content[:50] + '...'



    
