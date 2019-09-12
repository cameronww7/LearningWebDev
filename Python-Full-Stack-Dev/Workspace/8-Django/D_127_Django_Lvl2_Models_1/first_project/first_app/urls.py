from django.urls import path
from . import views

# adding urlpatterns
urlpatterns = [
    path('', views.index, name='index'),
]
