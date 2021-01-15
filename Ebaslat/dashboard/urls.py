from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('orders', views.order, name = 'orders'),
    path('products', views.product, name = 'orders'),
    path('customers', views.customer, name = 'orders'),
    path('marketing', views.marketing, name = 'orders'),
    path('customize_store', views.customize_store, name = 'orders'),
    path('analytics', views.analytics, name = 'orders'),
    path('settings', views.settings, name = 'orders'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
