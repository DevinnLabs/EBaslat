from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth, messages
from django.contrib.auth import login
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

def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is None:
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('dashboard/home')

    else:    
        return render(request, 'main/login.html')

def register(request):
    # if (request.method == 'POST'):
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
        
    #     if (password == confirm_password):
    #         if (User.objects.filter(username= username)):
    #             pass
    #         elif (User.objects.filter(email= email)):
    #             pass
    #         else:
    #             user = User.objects.create_user(username= username, email= email, password= password, first_name= first_name, last_name= last_name)
    #             user.save();

    # else:
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
