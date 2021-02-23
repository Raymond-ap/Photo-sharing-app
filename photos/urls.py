from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('post', post, name='post'),
    path('detail/<slug:slug>', detail, name='detail'),
]


"""
0263445140
{% static "img" as baseUrl %} 
"""