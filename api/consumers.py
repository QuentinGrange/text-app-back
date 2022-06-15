# chat/consumers.py
import json

from django.contrib.auth import get_user_model

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from api.models.message import Message
from api.serializers.user import UserSerializer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.conversation_group_name = 'chat_%s' % self.conversation_id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.conversation_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.conversation_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        response = {
            'type': text_data_json.get('type'),
        }

        if text_data_json.get('type') == 'create':
            new_message = Message(text=text_data_json['text'], user_id=text_data_json['user'],
                                  conversation_id=text_data_json['conversation'])
            new_message.save()

            response['id'] = str(new_message.id)
            response['text'] = text_data_json['text']
            response['conversation'] = text_data_json['conversation']
            response['user'] = UserSerializer(instance=get_user_model().objects.get(pk=text_data_json['user'])).data

        elif text_data_json.get('type') == 'edit':
            message = Message.objects.get(pk=text_data_json['id'])
            message.text = text_data_json['text']

            response['id'] = text_data_json['id']
            response['text'] = text_data_json['text']
            response['conversation'] = text_data_json['conversation']
            response['user'] = UserSerializer(instance=get_user_model().objects.get(pk=text_data_json['user'])).data

            message.save()

        elif text_data_json.get('type') == 'delete':
            Message.objects.get(pk=text_data_json['id']).delete()

            response['id'] = text_data_json['id']

        elif text_data_json.get('type') == 'writing':
            response['user'] = UserSerializer(instance=get_user_model().objects.get(pk=text_data_json['user'])).data

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.conversation_group_name,
            response
        )

    # Receive message from room group
    def create(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'create',
            'text': event['text'],
            'conversation': event['conversation'],
            'user': event['user'],
        }))

    def edit(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'edit',
            'id': event['id'],
            'text': event['text'],
            'conversation': event['conversation'],
            'user': event['user'],
        }))

    def delete(self, event):

        self.send(text_data=json.dumps({
            'type': 'delete',
            'id': event['id']
        }))

    def writing(self, event):

        self.send(text_data=json.dumps({
            'type': 'writing',
            'user': event['user']
        }))

    def writing_end(self, event):

        self.send(text_data=json.dumps({
            'type': 'writing_end',
        }))