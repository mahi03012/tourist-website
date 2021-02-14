from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']

        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            else:

                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1,)
                user.save()
                return redirect('login')

                    
        else:
            messages.info(request,'password didnt match')
        
        
    return render (request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pass1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid password')
            return redirect('login')
    else:
        return render (request,'login.html')

def details(request):
    database_info=User.objects.values("username","email")
    return render(request,"details.html",{"datas":database_info})

def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
