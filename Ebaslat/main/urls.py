from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about_us', views.about, name = 'about'),
    path('pricing', views.pricing, name = 'pricing'),
    path('features', views.features, name = 'features'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
    path('login', views.login, name = 'login'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
