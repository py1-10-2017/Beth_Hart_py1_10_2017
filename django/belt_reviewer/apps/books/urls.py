from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='home'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^show/(?P<book_id>\d+)$', views.show, name='show'),
    url(r'^update/(?P<book_id>\d+)$', views.update, name='update'),
    
    
    
    ]