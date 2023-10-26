from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def user_profile(request,pk):
    #get the data from user model and render it
    return render(request, 'index.html', {'user':request.user})


# signup page
def user_signup(request):
    if request.method == 'POST':
        # add validation logic here
        # 1.proper email
        # 2.confirma password and paswword are same
        username=request.POST["username"]
        password=request.POST["password"]
        confirmpassword=request.POST["confirm-password"]
        email=request.POST["email"]
        User = get_user_model()
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'signup.html')

# login page
def user_login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                redirect_url = reverse('index', args=[user.id])
                return HttpResponseRedirect(redirect_url)
            else:
                return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    

def user_logout(request):
    pass



