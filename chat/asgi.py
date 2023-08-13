import os
import app.routing

from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(app.routing.websocket_urlpatterns))
        ),
    }
)
