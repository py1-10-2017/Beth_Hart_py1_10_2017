'''users_app urls config'''

from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.index, name='index')
    ]
