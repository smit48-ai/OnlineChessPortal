import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from ChessGame.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineChessPortal.settings')



ws_pattern = [
    path('ws/game/<room_code>/' , GameRoom.as_asgi())
]


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(
            ws_pattern
        ))

})