from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def pricing(request):
    return render(request, 'main/pricing.html')

def features(request):
    return render(request, 'main/features.html')

def blog(request):
    return render(request, 'main/blog.html')

def contact(request):
    return render(request, 'main/contact.html')

def register(request):
    # form = CreateUserForm()
    form = CreateUserForm()

    if (request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('dashboard/home')

    context = {'form': form}
    return render(request, 'main/register.html', context= context)

def questionaire1(request):
    return render(request, 'main/questionaire1.html')

def questionaire2(request):
    return render(request, 'main/questionaire2.html')

# def loginPage(request):
    #     if (request.method == 'POST'):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username = username, password = password)
#         if user is None:
#             messages.info(request, "Username or password is incorrect")
#         else:
#             auth.login(request, user)
#             return redirect('dashboard/home')
  
#     return render(request, 'main/login.html', context=context)

# def logoutUser(request):
#     logout(request)
#     return redirect('/')
