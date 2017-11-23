# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
regex_obj = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class RegistrationManager(models.Manager):
    def regvalidation(self, regdata):
        errors = []
        if len(regdata['first_name']) < 2 or len(regdata['last_name']) < 2:
            errors.append('First and last name must be at least 2 characters in length.')
        if not regex_obj.match(regdata['email']):
            errors.append('Please enter a valid email address')
        if len(regdata['password1']) < 8 or regdata['password1'] != regdata['password2']:
            errors.append('Password must be at least 8 characters long and match')
        if User.objects.filter(email=regdata['email']).exists():
            errors.append("This email address is already registered with a user.")
        return errors

        
class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=55)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = RegistrationManager()

