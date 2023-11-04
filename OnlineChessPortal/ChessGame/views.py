from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from 
from django.contrib import messages
from .models import GameModel
from .models import *
from django.contrib.auth import get_user_model
import json



# samjo have
# 1.tamre eko to positions store karvi padse etle koi join thay to game ane board banne ma ej position
# thi start thay

# 2.game nu status rakhvu padse kem etla mate kem ke 
#     1.game draw thai sake
#     2.game win thai sake
#     3.game chalu hoy ya
#     4.game ma thi resgin thai gaya hoy
#  dar move e badhane mokal vanu to khara j pan simulentosly jovanu ke su
# thay che game pati to nathi ne ane message recieve karo tya status check karvanu agar game pati hoy oy
# to e pramane winner set karvano
#3.winner kon?? simple status ma username mokali devanu?? e kai rite khbr pade jeno turn hoy e losser
#4.elte je status recieve thu e pramane user ni ratings bhi badli devani like status draw hoy to banne ma +20 ane ek ma
#  ya to winner ne
#5.have main resgin kai rite jovo resgin ma simple law jevu user resgin dabave tarat j message jay
#  status update thai jay ke resgin che to same vado winner(tunka ma resgin - username mokalvanu)
#
#6.bijo mudo game pati ya resgin thai to dialog bok batavnu kai rite message send karvano hoy 
# consumer ma thi e bij method ne kol karavno che badjane mokal ane plus e je mokle ene acces karavnu
# ane e pramane dialog box render kardevano
#7.jevu dialog box close thay etle redirect kar devanu index
#8.refresh ma best che ke alert moklo ke resgin thai jase ane resgin vadu call kardo


def playView(request):
    if request.method=="POST":
        print("called")
        player2=request.POST.get('Player2')
        CustomUser=get_user_model()
        try:
            player1 = CustomUser.objects.get(username=request.user)
            player2 = CustomUser.objects.get(username=player2)
            game=GameModel(player1Id=player1,player2Id=player2,winner=player1,position='start')
            game.save()
            print(game.position)
            context={
                'player1':player1,
                'player2':player2,
                'code':game.id,
                'position':game.position,
                'gamestatus':game.status
            }
            return render(request,'game.html',context)
        except Exception as e:
            print(e)
            messages.error(request,"username does not exists")

    return redirect('index',request.user.id)


def joinView(request):
    if request.method=="POST":
        print("called these view")
        room_code=request.POST.get('code')
        try:
            game = GameModel.objects.get(id=room_code)
            print(game.position)
            context={
                'player1':game.player1Id,
                'player2':game.player2Id,
                'code':game.id,
                'position':game.position,
                'gamestatus':game.status
            }
            # print(context.position)
            return render(request,'game.html',context)
        except Exception as e:
            messages.error(request,"room does not exists")

    return redirect('index',request.user.id)
