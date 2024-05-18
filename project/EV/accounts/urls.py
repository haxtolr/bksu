# accounts/urls.py
from django.urls import path
from . import views
from main.views import main
from .views import UserLoginView, UserSignupView, UserLogoutView, MyInfoView


urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('main/', main, name='main'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('my_info/<str:username>/', MyInfoView.as_view(), name='my_info'),
]