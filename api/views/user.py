from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response

from api.serializers.user import UserSerializer, RegisterSerializer


class RegisterViewSet(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        print("data", request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully",
        })


class UserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
