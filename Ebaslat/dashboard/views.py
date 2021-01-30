from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, auth
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .decorators import UnauthenticatedUser
from .forms import *

# Create your views here.
@login_required(login_url = 'login')
def home(request):
    return render(request, 'dashboard/home.html')

@login_required(login_url = 'login')
def order(request):
    return render(request, 'dashboard/order.html')

@login_required(login_url = 'login')
def product(request):
    return render(request, 'dashboard/product.html')

@login_required(login_url = 'login')
def customer(request):
    return render(request, 'dashboard/customer.html')

@login_required(login_url = 'login')
def marketing(request):
    return render(request, 'dashboard/marketing.html')

@login_required(login_url = 'login')
def customize_store(request):
    return render(request, 'dashboard/customize_store.html')

@login_required(login_url = 'login')
def analytics(request):
    return render(request, 'dashboard/analytics.html')

@login_required(login_url = 'login')
def settings(request):
    return render(request, 'dashboard/settings.html')

@UnauthenticatedUser
def loginPage(request):

    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is None:
            messages.info(request, "Username or password is incorrect")
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('home')
  
    context = {}
    return render(request, 'main/login.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('../')