from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from ChessGame.models import GameModel
from tournaments.models import Tournament
from django.contrib import messages
from django.core.mail import send_mail
import json

@login_required
def user_profile(request,pk):
    #get the data from user model and render it
    # messages.get_messages(request)
    print("message is --> ",messages)
    CustomUser = get_user_model()
    Allusers = CustomUser.objects.all()
    Allgames = GameModel.objects.all()
    # print(request.user.username)
    CurrentUser=CustomUser.objects.get(username=request.user.username)
    wins=0
    lose=0
    draw=0
    # print(CurrentUser)
    tournaments=Tournament.objects.all()
    tournamentDetails=[]
    for tournament in tournaments:
        count=len(json.loads(tournament.users))
        curr={
            'Name':tournament.Name,
            'count':count,
            'id':tournament.id
        }
        tournamentDetails.append(curr)

    for game in Allgames:
        print(game.winner)
        if game.winner==CurrentUser:
            wins=wins+1
        if game.winner!=CurrentUser and (game.player1Id==CurrentUser or game.player2Id==CurrentUser):
            lose=lose+1
        if game.winner=="" and (game.player1Id==CurrentUser or game.player2Id==CurrentUser):
            draw=draw+1
    context={
        'user':request.user,
        'Allusers':Allusers,
        'wins':wins,
        'lose':lose,
        'draw':draw,
        'tournaments':tournamentDetails
    } 
    return render(request, 'index.html', context)


def uploadProfile(request):
    CustomUser = get_user_model()
    if request.method == 'POST' and request.FILES['profile_picture']:
        profile_pic = request.FILES['profile_picture']
        profile = CustomUser.objects.get_or_create(username=request.user)[0]
        profile.profile_picture = profile_pic
        profile.save()
    
    return redirect('index',request.user.id)

# signup page
def user_signup(request):
    
    if request.method == 'POST':
        # add validation logic here
        # 1.proper email
        # 2.confirma password and paswword are same
        username=request.POST["username"]
        password=request.POST["password"]
        confirmpassword=request.POST["confirm-password"]
        if password==confirmpassword:
            email=request.POST["email"]
            try:
                User = get_user_model()
                user=User.objects.create_user(username,email,password)
                user.is_active = False 
                user.save()
                token = user.generate_verification_token()
                verification_link = f"http://127.0.0.1:8000/accounts/verify/{token}/"
                send_mail(
                    'Verify your email',
                    f'Click the following link to verify your email: {verification_link}',
                    'mailservice2422@gmail.com',
                    [user.email],
                    fail_silently=False,
                )
                return redirect('login')
            except Exception as e:
                messages.error(request,"Username already exists")
        else:
            messages.error(request,"password and confirm password is not same")
    
    return render(request, 'signup.html')



# login page
def user_login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)  
                redirect_url = reverse('index', args=[user.id])
                return HttpResponseRedirect(redirect_url)
            elif user and user.is_active==False:
                messages.error(request,"Email is not verified")
                return render(request, 'login.html')
            else:
                messages.error(request,"username or password is wrong")
                return render(request, 'login.html')
    else:
       messages.get_messages(request).used = True
       return render(request, 'login.html')
    

def user_logout(request):
    logout(request)
    return render(request,'login.html')


def verify_email(request, token):
    CustomUser = get_user_model()
    user = CustomUser.objects.filter(verification_token=token).first()
    if user:
        user.email_verified = True
        user.is_active=True
        user.save()
        login(request, user)
        redirect_url = reverse('index', args=[user.id])
        return HttpResponseRedirect(redirect_url)
    else:
        return render(request, 'accounts/verification_failure.html')
