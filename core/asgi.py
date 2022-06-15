# """
# ASGI config for core project.
#
# It exposes the ASGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
# """
#
# import os
#
# import django
#
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import api.routing
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# django.setup()
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             api.routing.websocket_urlpatterns
#         )
#     ),
# })

import os
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_default_application()
