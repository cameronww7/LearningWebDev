# Created in lecture 121 URL Mapping
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
