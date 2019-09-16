from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    # Create new User form
    form = NewUserForm()

    # if someone hits sumbit we check
    if request.method == "POST":
        form = NewUserForm(request.POST)

        # If is valid, we save the form
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'appTwo/users.html',{'form':form})
