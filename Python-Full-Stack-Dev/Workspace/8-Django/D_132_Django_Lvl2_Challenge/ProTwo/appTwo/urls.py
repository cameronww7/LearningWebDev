from django.conf.urls import url
from appTwo import views # Need to Import

# Drop the url pattern list
urlpatterns = [
    url(r'^$',views.users,name='users'),
]
