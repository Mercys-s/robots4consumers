from django.urls import path

from .views import *



urlpatterns = [
    path('', create_order, name = 'create_order')
]