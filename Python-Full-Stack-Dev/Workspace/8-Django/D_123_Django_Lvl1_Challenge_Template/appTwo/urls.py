from django.urls import path
from . import views

# have to add the url path to find the page
urlpatterns = [
    path('', views.help, name='help'),
]
