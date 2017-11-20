"""users app models"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
regex_obj = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserFormManager(models.Manager):
    def validate_fields(self, form_data):
        
        errors=[]
        if len(form_data['first_name']) < 1 or len(form_data['last_name'])< 1:
            errors.append('First and last name are required!')
        if not regex_obj.match(form_data['email']):
            errors.append('Please enter a valid email address')
        if User.objects.filter(email=form_data['email']).exists:
            #===================
            #need to add hidden input in edit form, to identify if email address of existing id is the same as updating id
            errors.append('Email address is already registered by another user.')
        return errors    



class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserFormManager()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
