from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


from enroll.forms import SignUpForm
from django.contrib import messages


def welcome(request):
    return render(request, 'enroll/welcome.html')

def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'user creates successfully')
            fm.save()
    else:
        fm = SignUpForm
    return render(request, 'enroll/sign_up.html', {'fm': fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully')
                    return HttpResponseRedirect('/enroll/profile/')
        else:
            fm = AuthenticationForm
        return render(request, 'enroll/user_login.html', {'form': fm})
    else:
        return redirect('/enroll/profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return redirect('/enroll/user_login')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/user_login')

def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/enroll/profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'enroll/changepass.html', {'form': form})
    else:
        return redirect('/enroll/user_login')
# Create your views here.
