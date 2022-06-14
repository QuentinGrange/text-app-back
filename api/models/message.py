from django.db import models
from django.contrib.auth import get_user_model

import uuid


class Message(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    text = models.TextField(verbose_name='Text')
    user = models.ForeignKey(get_user_model(), related_name='messages', on_delete=models.CASCADE)
    conversation = models.ForeignKey('api.Conversation', related_name='messages', on_delete=models.CASCADE, null=True)
