from django.urls import path

from .views import *



urlpatterns = [
    path('', create_robots, name = 'create_robots')
]