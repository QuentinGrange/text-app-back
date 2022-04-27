from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend


from api.models import Story
from api.serializers import StorySerializer
from api.filters import StoryFilter


class StoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StorySerializer
    queryset = Story.objects.all()
    search_fields = ('conversation', )
    ordering_fields = ('id',)
    ordering = ('id',)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, ]
    filter_class = StoryFilter


