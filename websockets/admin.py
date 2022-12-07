from django.contrib import admin
from .models import Chat, Group, GroupMember
# Register your models here.

class AdminChat(admin.ModelAdmin):
    list_display = ['user','content','group','timestamp']

admin.site.register(Group)
admin.site.register(Chat,AdminChat)

@admin.register(GroupMember)
class AdminGroupMember(admin.ModelAdmin):
    list_display = ['group']
