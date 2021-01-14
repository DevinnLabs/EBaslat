from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about.html', views.about, name = 'about'),
    path('pricing.html', views.pricing, name = 'pricing'),
    path('features.html', views.features, name = 'features'),
    path('blog.html', views.blog, name = 'blog'),
    path('contact.html', views.contact, name = 'contact'),
    path('login.html', views.login, name = 'login'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
