from django.db import models

# Create your models here.

class Conversation(models.Model):
    sender = models.CharField(max_length=200)
    created = models.DateTimeField('date created')
    conversation_id = models.CharField(max_length=200)
    message = models.TextField()

