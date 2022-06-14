from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/conversation/(?P<conversation_id>[^/.]+)/', ChatConsumer.as_asgi()),
]