from django.contrib.auth import get_user_model

import django_filters
from django_filters.rest_framework import BaseInFilter, NumberFilter


class IdInFilter(BaseInFilter, NumberFilter):
    pass


class UserFilter(django_filters.FilterSet):
    id__in = IdInFilter(field_name="id", lookup_expr="in")

    class Meta:
        model = get_user_model()
        fields = "__all__"
