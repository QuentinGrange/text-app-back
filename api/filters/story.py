import django_filters

from api.models import Story


class StoryFilter(django_filters.FilterSet):

    class Meta:
        model = Story
        fields = "__all__"
