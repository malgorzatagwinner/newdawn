# chat/middleware.py

from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async

@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()

class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return TokenAuthMiddlewareInstance(scope, self.inner)

class TokenAuthMiddlewareInstance:
    def __init__(self, scope, inner):
        self.scope = dict(scope)
        self.inner = inner

    async def __call__(self, receive, send):
        query_string = self.scope.get("query_string", b"").decode()
        params = parse_qs(query_string)
        token = params.get("token", [None])[0]

        self.scope["user"] = await get_user(token)
        inner = self.inner(self.scope)
        return await inner(receive, send)

