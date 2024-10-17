from django.shortcuts import render
from . import forms

def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    return render(request, 'formsDemo/userRegistration.html', {'form': form})
