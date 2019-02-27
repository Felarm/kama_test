__author__ = 'Андрей'

from django.conf.urls import url, include
from . import views

app_name = 'URLshortener'
urlpatterns = [
    url(r'^$', views.shortener, name='shortener'),
    url(r'^(?P<short_part>.{3})$', views.redirect, name='redirect'),
]