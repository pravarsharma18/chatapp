from django.shortcuts import render
from .models import Group, Chat
# Create your views here.

def homepage(request, group_name):
    group, created = Group.objects.get_or_create(name=group_name)
    chats = group.chat.all()
    context = {
        "group_name":group.name,
        "chats":chats
    }
    return render(request, "websockets/index.html", context)