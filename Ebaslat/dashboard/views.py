from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dashboard.html')

def order(request):
    return render(request, 'order.html')

def product(request):
    return render(request, 'product.html')

def customer(request):
    return render(request, 'customer.html')

def marketing(request):
    return render(request, 'marketing.html')

def customize_store(request):
    return render(request, 'customize_store.html')

def analytics(request):
    return render(request, 'analytics.html')

def settings(request):
    return render(request, 'settings.html')