from django import forms

class UserRegistrationForm(forms.Form):
    first_Name = forms.CharField()
    last_Name = forms.CharField()
    email = forms.CharField()