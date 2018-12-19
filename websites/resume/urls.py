from django.conf.urls import url
from websites.resume import views

# urlpatterns = [
#     path('', views.websites,),
# ]

urlpatterns = [
    url('', views.resume)
]