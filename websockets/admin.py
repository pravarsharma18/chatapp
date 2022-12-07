from django.contrib import admin
from .models import Chat, Group
# Register your models here.

class AdminChat(admin.ModelAdmin):
    list_display = ['user','content','timestamp']

admin.site.register(Group)
admin.site.register(Chat,AdminChat)
