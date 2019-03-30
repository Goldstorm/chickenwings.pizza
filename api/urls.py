from django.conf.urls import re_path

from api import views

urlpatterns = [
    re_path(r'^(?P<param1>[^/]+)/?', views.ApiProcessor.as_view()),
]