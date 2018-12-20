import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from twisted.protocols.memcache import ClientError

from .models import AuctionReady, Auction

class AuctionConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        url = self.channel_name
        print(url)
        auction_room = "auction"
        self.auction_room = auction_room
        await self.channel_layer.group_add(
            auction_room,
            self.channel_name
        )
        print(self.channel_layer.group_add)
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        #when a auction is received from the websocket
        print("receive", event)
        front_text = event.get('text', None)
        if front_text is not None:
            loaded_dict_data = json.loads(front_text)
            print(loaded_dict_data)
            price = loaded_dict_data.get('price')
            auction_id = loaded_dict_data.get('id')
            print(auction_id)
            user = self.scope['user']
            username = 'unknown'
            ref = Auction.objects.get(id=auction_id)
            if user.is_authenticated:
                username = user.username
                await self.create_auctio_ready(user, price, ref)
            await self.channel_layer.group_send(
                self.auction_room,
                {
                "type": "auction_price",
                'price': "₺" + price + " " + username + "@" + auction_id,
                }
            )

    async def auction_price(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['price'],
        })

    async def websocket_disconnect(self, event):
        #when the socket connects
        print("disconnected", event)

    @database_sync_to_async
    def get_auction_or_error(self):
        return Auction.group_name()


    @database_sync_to_async
    def create_auctio_ready(self, user, price, ref):
        return AuctionReady.objects.create(auction_ref=ref, user_ref=user, auction_price=price)
