from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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
    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done', auth_views.PasswordResetDoneView.as_view(), name="reset_password_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
