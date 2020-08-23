from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import logout as django_logout
from . models import Questions
from .forms import exmForm
from datetime import timedelta


# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'portal/index.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('rules')
    else:
        form = SignUpForm()
    return render(request, 'portal/signup.html', {'form': form})




def rules(request):
    if request.user.is_authenticated:
        return render(request, 'portal/rules.html')
    else:
        return redirect( 'index')





@login_required
def logout(request):
    django_logout(request)
    return render(request, 'portal/rules.html')



def quiz(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = exmForm(request.POST)
            if form.is_valid():
                u = form.save()
                django_logout(request)

                return render(request, 'portal/endexm.html')
        else:
            form = exmForm()
        return render(request, 'portal/question.html', {'form': form})
    else:
        return redirect('index')


def endexm(request):
    if request.user.is_authenticated:
        return render(request, 'portal/endexm.html')
    else:
        return redirect('/portal/index')