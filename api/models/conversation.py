from django.db import models
from django.contrib.auth import get_user_model

import uuid


class Conversation(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(verbose_name='Name', max_length=255)
    users = models.ManyToManyField(get_user_model(), related_name='conversations')
