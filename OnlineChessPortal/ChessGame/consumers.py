from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync  
from .models import GameModel
import json




class GameRoom(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room = None

    def connect(self):
        print("hi")
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' % self.room_name
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print("it works")
        
        self.accept()

        
    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    def receive(self , text_data):
        print(text_data)
        received_data = json.loads(text_data)
        print(received_data['data']['position'])
        try:
            game = get_object_or_404(GameModel, pk=received_data['data']['code'])
          
            game.position=received_data['data']['position']
            CustomUser=get_user_model()
            player1=game.player1Id
            player2=game.player2Id
            
            if(received_data['data']['status']['status']=="complete"):
                username=received_data['data']['status']['winner']
                if(username!="draw"):
                    winner=CustomUser.objects.get(username=username)
                    winner.Rating=winner.Rating+20
                    if(player1==winner):
                        player2.Rating-=20
                    if(player2==winner):
                        player1.Rating-=20
                    player1.save()
                    player2.save()
                    winner.save()
                else:
                    player1+=20
                    player2+=20
                    player1.save()
                    player2.save()
                    winner=""
                game.status="complete"
                game.winner=winner
            if(received_data['data']['status']['status']=="resgin"):
                username=received_data['data']['status']['winner']
                winner=CustomUser.objects.get(username=username)
                winner.Rating=winner.Rating+20
                if(player1==winner):
                    player2.Rating-=20
                if(player2==winner):
                    player1.Rating-=20
                player1.save()
                player2.save()
                winner.save()
                game.status="resgin"
                game.winner=winner
            game.save()
        except Exception as e:
            print(e)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type' : 'run_game',
                'payload' : text_data,
                "sender_channel_name": self.channel_name 
            }
        )
        
    
    def run_game(self , event):
        data = event['payload']
        data = json.loads(data)
        sender_channel_name = event["sender_channel_name"]

        if sender_channel_name != self.channel_name:
            self.send(text_data=json.dumps({
                    'payload' : data['data']
                }))        
        
         