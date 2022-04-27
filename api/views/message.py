from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend


from api.models import Message
from api.serializers import MessageSerializer
from api.filters import MessageFilter


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    search_fields = ('text',)
    ordering_fields = ('id',)
    ordering = ('id',)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filter_class = MessageFilter

