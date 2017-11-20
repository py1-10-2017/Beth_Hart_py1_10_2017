'''urls for courses app'''

from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<course_id>\d+)/destroy$', views.destroy, name='destroy'),
    url(r'^(?P<course_id>\d+)/warning$', views.warning, name='warning'),
    ]