from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<blog_id>\d+)$', views.show, name='show'),
    url(r'^(?P<blog_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<blog_id>\d+)/delete/$', views.destroy, name='destroy')
    ]
