from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def order(request):
    return render(request, 'dashboard/order.html')

def product(request):
    return render(request, 'dashboard/product.html')

def customer(request):
    return render(request, 'dashboard/customer.html')

def marketing(request):
    return render(request, 'dashboard/marketing.html')

def customize_store(request):
    return render(request, 'dashboard/customize_store.html')

def analytics(request):
    return render(request, 'dashboard/analytics.html')

def settings(request):
    return render(request, 'dashboard/settings.html')