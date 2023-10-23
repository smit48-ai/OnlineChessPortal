from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model






# signup page
def user_signup(request):
    if request.method == 'POST':
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
                return redirect('index')
            else:
                return render(request, 'login.html')
    else:
        return render(request, 'login.html')
