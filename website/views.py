from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home (request):
    #checking to see if log in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, Please try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    logout(request,)
    messages.success(request, "you have been logged out...")
    return redirect('home')

def logout_user(request):
    logout(request,)
    messages.success(request, "you have been logged out...")
    return redirect('home')


# Create your views here.
def register_user(request):
    return render(request, 'register.html', {})