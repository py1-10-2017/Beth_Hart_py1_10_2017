'''urls for users app'''
from django.conf.urls import url 
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>\d+)/$', views.show, name='show'),
    url(r'^new$', views.new, name='new'),
    url(r'^(?P<user_id>\d+)/edit$', views.edit, name='edit'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<user_id>\d+)/delete', views.delete, name='destroy')
    ]

