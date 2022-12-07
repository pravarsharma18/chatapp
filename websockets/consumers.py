
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from django.contrib.auth import get_user_model
from .models import Chat, Group, GroupMember
from channels.db import database_sync_to_async

User = get_user_model()

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("connected....", event)
        print("channel_layer", self.channel_layer)
        print("channel_name", self.channel_name)
        self.groupname = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(self.groupname, self.channel_name)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print("Recieved....", event)
        data = json.loads(event['text'])
        chat = Chat()
        print(Group.objects.get(name=self.groupname), "********************")
        print(User.objects.get(username=data['user']), "********************")
        chat.content = data['msg']
        chat.group = Group.objects.get(name=self.groupname)
        chat.user = User.objects.get(username=data['user'])
        chat.save()
        async_to_sync(self.channel_layer.group_send)(self.groupname, {
            'type':'chat.message',
            'message':event['text']
        })
    
    def chat_message(self, event):
        print("event...", event)
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })

    def websocket_disconnect(self, event):
        print("Disconnected.....", event)
        print("channel_layer", self.channel_layer)
        print("channel_name", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.groupname, self.channel_name)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("connected....", event)
        print("channel_layer", self.channel_layer)
        print("channel_name", self.channel_name)
        print("self.scope.....",self.scope['url_route']['kwargs'])
        self.groupname = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(self.groupname, self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print("Recieved....", event)
        data = json.loads(event['text'])
        user = await database_sync_to_async(User.objects.get)(username=data['user'])
        group = await database_sync_to_async(Group.objects.get)(name=self.groupname)
        chat = Chat()
        chat.content = data['msg']
        chat.group = group
        chat.user = user
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(self.groupname, {
            'type':'chat.message',
            'message':json.dumps(chat.content),
            # 'timestamp':json.dumps(chat.timestamp, default=str),
            'user':json.dumps(chat.user.username, default=str)
        })
    
    async def chat_message(self, event):
        print("event...", event)
        await self.send({
            'type':'websocket.send',
            'text':event['message'],
        })

    async def websocket_disconnect(self, event):
        print("Disconnected.....", event)
        print("channel_layer", self.channel_layer)
        print("channel_name", self.channel_name)
        await self.channel_layer.group_discard(self.groupname, self.channel_name)
        raise StopConsumer()