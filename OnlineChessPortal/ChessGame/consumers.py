from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync  
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
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type' : 'run_game',
                'payload' : text_data
            }
        )
        
    
    def run_game(self , event):
        data = event['payload']
        data = json.loads(data)

        self.send(text_data=json.dumps({
            'payload' : data['data']
        }))        
        
         