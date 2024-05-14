# accounts/urls.py
from django.urls import path
from . import views
from main.views import main
from .views import UserLoginView, UserSignupView, UserLogoutView


urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('main/', main, name='main'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]