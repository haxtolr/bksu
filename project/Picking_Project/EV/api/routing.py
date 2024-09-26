# routing.py

from django.urls import re_path
from .consumers import Send_rackConsumer

websocket_urlpatterns = [
    re_path(r'ws/send_rack/$', Send_rackConsumer.as_asgi()),
]
