
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import websockets.routings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sockets.settings')
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':URLRouter(websockets.routings.websocket_urlpatterns)
})
