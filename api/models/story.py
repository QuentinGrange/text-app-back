from django.db import models
from django.contrib.auth import get_user_model

import uuid


class Story(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(verbose_name='Name', max_length=255)
    user = models.ForeignKey(get_user_model(), related_name='stories', on_delete=models.CASCADE)
    conversation = models.ForeignKey('api.Conversation', related_name='stories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
