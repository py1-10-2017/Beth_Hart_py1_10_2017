# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Description(models.Model):
    text = models.TextField(primary_key=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description)
    created_at= models.DateTimeField(auto_now_add=True)
    
