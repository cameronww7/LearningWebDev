from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

# Takes in users password
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    # Basic meta information about user
    class Meta():
        model = User
        fields = ('username','email','password')

# basic user pofile relationship
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
