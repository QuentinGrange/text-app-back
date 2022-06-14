from rest_framework import serializers

from rest_flex_fields import FlexFieldsModelSerializer

from api.models import Message


class MessageSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        expandable_fields = {
            'user': 'api.UserSerializer'
        }
