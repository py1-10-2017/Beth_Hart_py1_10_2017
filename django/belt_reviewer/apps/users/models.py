# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=55)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

