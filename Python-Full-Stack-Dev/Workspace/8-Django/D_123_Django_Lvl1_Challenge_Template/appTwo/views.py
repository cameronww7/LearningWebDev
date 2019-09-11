from django.shortcuts import render
from django.http import HttpResponse

# Spits out My Second Project
def index(request):
    return HttpResponse("<em>My Second Project</em>")

# Adds Help Page
def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)
