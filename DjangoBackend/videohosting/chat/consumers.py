import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        response = json.loads(text_data)
        event = response.get("event", None)
        text = response.get("text", None)
        if event == 'MESSAGE':
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'event': event,
                'text': text
            })

    async def send_message(self, res):
        await self.send(text_data=json.dumps({
            "payload": res,
        }))
