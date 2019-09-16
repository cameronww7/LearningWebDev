from django import forms
from django.core import validators

# After creating Temple Now need to Create Forms

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name Doesnt start with Z")

# Class of Form
class FormName(forms.Form):
    """
    Class for Form, used to take in the data from the Form
    """
    name         = forms.CharField()
    email        = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text         = forms.CharField(widget=forms.Textarea)

    # Catches Bots, if a bot inspects the page they will try to Fill
    # values on the html page however this will prevent that.
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    #  validators=[validators.MaxLengthValidator(0)])
    # This works like the function below but must easier


    # def clean_botcatcher(self):
    # """
    # Catches a bot and prevents them from submitting
    # """
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")



    def clean(self):
        """
        Checks to make sure emails match and will clear if they dont
        """
        all_clean_data = super().clean()

        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
