from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, mixins, viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from django_filters.rest_framework import DjangoFilterBackend

from api.serializers.user import UserSerializer, RegisterSerializer


class RegisterViewSet(generics.GenericAPIView):

    queryset = get_user_model().objects.all()
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


class UserAPIView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    search_fields = ('name',)
    ordering_fields = ('id',)
    ordering = ('id',)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]

