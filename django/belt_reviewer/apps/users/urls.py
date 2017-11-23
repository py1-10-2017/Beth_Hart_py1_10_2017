from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^(?P<user_id>\d+)$', views.show, name='show'),
    url(r'^register$', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    ]