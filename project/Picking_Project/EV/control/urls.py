from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # urls.py
    path('trigger_message/', views.trigger_message, name='trigger_message'),
]

