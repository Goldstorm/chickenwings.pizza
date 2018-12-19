from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import generics
from . import views

# urlpatterns = [
#     path('', views.website,),
# ]

urlpatterns = [
    url('', views.cwp)
]