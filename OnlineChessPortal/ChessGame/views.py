from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def playView(request):
    
    return render(request,"game.html",{})

