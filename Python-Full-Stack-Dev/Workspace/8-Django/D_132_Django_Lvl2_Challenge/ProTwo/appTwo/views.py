from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User # import appTwo
# Create your views here.

# views of apptwo - This is the Home Page
def index(request):
    return render(request,'apptwo/index.html')


# Displays the users and their data
def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'apptwo/users.html',context=user_dict)
