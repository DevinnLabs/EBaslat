from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('orders', views.order, name = 'orders'),
    path('products', views.product, name = 'products'),
    path('customers', views.customer, name = 'customers'),
    path('marketing', views.marketing, name = 'marketing'),
    path('customize_store', views.customize_store, name = 'customize_store'),
    path('analytics', views.analytics, name = 'analytics'),
    path('settings', views.settings, name = 'settings'),
    path('login', views.loginPage, name = 'login'),
    path('logout', views.logoutUser, name = 'logout'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
