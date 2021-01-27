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
    path('register', views.register, name = 'register'),
    path('questionaire1', views.questionaire1, name = 'questionaire1'),
    path('questionaire2', views.questionaire2, name = 'questionaire2'),
    # path('login', views.loginPage, name = 'login'),
    # path('logout', views.logoutUser, name = 'logout'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
