from django.shortcuts import render
from .models import Tournament
from ChessGame.models import GameModel
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

# Create your views here.


def CreateContest(request):
    #get form details
    #matches = n*(n-1)
    #generate all matches 
    #create 
    if request.method=="POST":
        TournamentName=request.POST['name']
        userlist=[]
        x=1
        while(1):
            if "username "+str(x) in request.POST:
                userlist.append(request.POST["username "+str(x)])
                x+=1
            else:
                break
       
        print(type(userlist))
        n=len(userlist)
        CustomUser=get_user_model()
        gameIds=[]
        for x in range(n):
            for y in range(n-x-1):
                player1=CustomUser.objects.get(username=userlist[x])
                player2=CustomUser.objects.get(username=userlist[x+y+1])
                newgame=GameModel(player1Id=player1, player2Id=player2)
                newgame.save()
                gameIds.append(newgame.id)
        newtournament=Tournament(Name=TournamentName,users=json.dumps(userlist),gameIds=json.dumps(gameIds),status="running")
        newtournament.save()
        redirect_url = reverse('Page', args=[newtournament.id])
        return HttpResponseRedirect(redirect_url)
    else:
        return render(request,'create.html')


    

def Detailsview(request,pk):
    # table 1 -  (player username played won lose draw)
    # table 2 - (shedule player1 player2 code)
    tournament=Tournament.objects.get(id=pk)
    # list of objects for players
    # list of objectd for games
    CustomUser=get_user_model()
    playerDetails={}
    gameDetails=[]
    players=json.loads(tournament.users)
    games=json.loads(tournament.gameIds)
    for player in players:
        newplayer={
             'win':0,
             'lose':0,
             'draw':0,  
             'points':0
        }
        playerDetails[player]=newplayer
    
    for game in games:
        print(game)
        gameobj=GameModel.objects.get(id=game)
        gameDetails.append(gameobj)
        if(gameobj.status=="complete" or gameobj.status=="resgin"):
            winner=gameobj.winner
            if(winner!=""):
                playerDetails[winner.username]['win']+=1
                playerDetails[winner.username]['points']+=7
                if(winner==gameobj.player1Id):
                    playerDetails[gameobj.player2Id.username]['lose']+=1
                    playerDetails[gameobj.player2Id.username]['points']-=2
                else:
                    playerDetails[gameobj.player1Id.username]['lose']+=1
                    playerDetails[gameobj.player1Id.username]['points']-=2
            else:
                playerDetails[gameobj.player2Id.username]['draw']+=1
                playerDetails[gameobj.player1Id.username]['draw']+=1
    playerDetails = dict(sorted(playerDetails.items(), key=lambda item: item[1]['points'],reverse=True))
    print(playerDetails)
    context={
        'name':tournament.Name,
        'playerDetails':playerDetails,
        'gameDetails':gameDetails
    }

    return render(request,"details.html",context)
        
        


