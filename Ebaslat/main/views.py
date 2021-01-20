from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth, messages

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
    return render(request, 'main/register.html')

def questionaire1(request):
    return render(request, 'main/questionaire1.html')

def questionaire2(request):
    return render(request, 'main/questionaire2.html')
