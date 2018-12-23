from django.urls import path
from django.contrib.auth import views as auth_views
from .views import auth

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('registration/', auth.UserRegistrationView.as_view(), name='registration'),
    # path('registration/', auth.registration, name='registration'),
]
