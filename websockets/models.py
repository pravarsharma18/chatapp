from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class GroupQuerySet(models.QuerySet):
    def members(self, name, user):
        return self.get(name=name, user=user).member.all()

    def chats(self, name, user):
        gm = GroupMember.objects.filter(group__name=name, user=user)
        if gm:
            return self.get(name=name, user=gm.first().group.user).chat.all()
        else:
            return False
        


class GroupManager(models.Manager):
    def get_queryset(self):
        return GroupQuerySet(self.model, using=self._db)

    def members(self, name, user):
        return self.get_queryset().members(name, user)
    
    def chats(self, name, user):
        return self.get_queryset().chats(name, user)

class Group(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group')

    objects = GroupManager()

    def __str__(self) -> str:
        return self.name

class Chat(models.Model):
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='chat')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat')
    timestamp = models.DateTimeField(auto_now_add=True)

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='member')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_member')
