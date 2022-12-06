from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=255)

class Chat(models.Model):
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='chat')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat')
    timestamp = models.DateTimeField(auto_now_add=True)
