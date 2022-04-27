import django_filters

from api.models import Conversation


class ConversationFilter(django_filters.FilterSet):

    class Meta:
        model = Conversation
        fields = "__all__"
