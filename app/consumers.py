import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def get_user(self):
        user = self.scope["user"]
        return user

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # Authenticate the user
        user = await self.get_user()
        if user.is_authenticated:
            # Associate the WebSocket connection with the user
            await self.channel_layer.group_add(user.username, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Remove the WebSocket connection from the user's group
        user = await self.get_user()
        if user.is_authenticated:
            await self.channel_layer.group_discard(user.username, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # Get the user who sent the message
        user = await self.get_user()
        username = user.username if user.is_authenticated else "Anonymous"

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, "username": username}
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        # Send message to WebSocket
        user = await self.get_user()
        if user.is_authenticated:
            if user.username == username:
                await self.send(text_data=json.dumps({"message": message, "username": "You"}))
            else:
                await self.send(text_data=json.dumps({"message": message, "username": username}))
