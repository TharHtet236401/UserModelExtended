from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'bio', 'password1', 'password2']
