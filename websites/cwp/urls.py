from django.conf.urls import url
from websites.cwp import views

# urlpatterns = [
#     path('', views.websites,),
# ]

urlpatterns = [
    url('', views.cwp)
]