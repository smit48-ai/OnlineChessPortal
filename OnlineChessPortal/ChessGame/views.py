from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from 
from django.contrib import messages
from .models import GameModel
from .models import *

@login_required
def playView(request):
    #from game
    # print(request.user)
    # user=
    # new_game=GameModel.ovj
    return render(request,'game.html')
    # if request.method == "POST":
    #     username = request.POST.get('username')
    #     option = request.POST.get('option')
    #     room_code = request.POST.get('room_code')
        
    #     if option == '1':
    #         game = Game.objects.filter(room_code = room_code).first()
            
    #         if game is None:
    #             message.success(request , "Room code not found")
    #             return redirect('/')
            
    #         if game.is_over:
    #             message.success(request , "Game is over")
    #             return redirect('/')
             
    #         game.game_opponent = username
    #         game.save()
    #     else:
    #         game = Game(game_creator = username , room_code = room_code)
    #         game.save()        
    #         return redirect('/play/' + room_code + '?username='+username)     
            
    # return render(request, 'home.html')
  
# def play(request , room_code):
#     username = request.GET.get('username')
#     context = {'room_code' : room_code , 'username' : username}
#     return render(request, 'play.html' , context)