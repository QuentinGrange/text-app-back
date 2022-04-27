from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import RegisterViewSet, UserAPIView, ConversationViewSet, MessageViewSet, StoryViewSet

router = routers.SimpleRouter()

router.register("conversations", ConversationViewSet)
router.register("messages", MessageViewSet)
router.register("stories", StoryViewSet)

urlpatterns = [
    path('v1/admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/auth/register/', RegisterViewSet.as_view(), name='register'),
    path('v1/users/', UserAPIView.as_view(), name='users'),
    path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
