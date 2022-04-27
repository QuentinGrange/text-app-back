import django_filters

from api.models import Message


class MessageFilter(django_filters.FilterSet):

    class Meta:
        model = Message
        fields = "__all__"
