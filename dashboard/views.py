from django.shortcuts import render
from django.views.generic import ListView
from websockets.models import GroupMember, Group



class HomePage(ListView):
    template_name = "dashboard/homepage.html"
    
    def get_queryset(self):
        return GroupMember.objects.filter(user = self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chats'] = Group.objects.chats(user = self.request.user, name=self.kwargs['group_name']).order_by('-timestamp')
        context['group_name'] = self.kwargs['group_name']
        return context 

