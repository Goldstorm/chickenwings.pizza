from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import generics

from . import views


urlpatterns = [
    url('^attempt/?(?P<param1>[^/]*)/?', views.API_PROCCESSOR.as_view())
]