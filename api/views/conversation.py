from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from django_filters.rest_framework import DjangoFilterBackend


from api.models import Conversation
from api.serializers import ConversationSerializer
from api.filters import ConversationFilter


class ConversationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
    search_fields = ('name',)
    ordering_fields = ('id',)
    ordering = ('id',)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filter_class = ConversationFilter


