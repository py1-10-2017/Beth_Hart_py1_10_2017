# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class dog(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    breed = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'dogs'
        
    def __str__(self):
        return self.name
    

