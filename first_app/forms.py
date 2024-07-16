from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        username = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
        first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
        last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
        email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))
        model = User
        fields = ['username','first_name','last_name','email']
        
        