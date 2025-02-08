from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login,logout
from django.contrib import messages


# Create your views here.
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Registration successful. Welcome!')
            return redirect('/')
        else:
            messages.error(request,'Registration failed. Please check the form.')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,'Logged in successfully.')
            return redirect('/')
        else:
            messages.error(request,'Error Logging in. Please try again.')
    else:
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successfully.')
    return redirect('/')
        
