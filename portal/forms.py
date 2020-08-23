from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Questions


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    post = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'post','password1', 'password2', )

class exmForm(forms.ModelForm):


    class Meta:
        model = Questions
        fields = '__all__'