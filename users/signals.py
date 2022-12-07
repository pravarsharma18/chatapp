from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from websockets.models import Group, GroupMember

User = get_user_model()

@receiver(post_save, sender=User)
def create_initial_group(sender, created, instance, **kwargs):
    if created:
        group_name = "Town-Square"
        g = Group.objects.create(name=group_name, user_id=instance.id)
        GroupMember.objects.create(group = g, user_id=instance.id)
        print(f"Group {group_name} Created for {instance.username}")