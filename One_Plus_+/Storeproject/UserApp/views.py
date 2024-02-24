from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django. contrib import messages,auth



# Create your views here.
def register(req):
    if req.method=='POST':
        fname=req.POST.get("fname","")
        lname=req.POST.get("lname","")
        email=req.POST.get("email","")
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        cpassword=req.POST.get("cpassword","")
        print(fname,lname,email,username,password,cpassword)
        if password==cpassword:
            print("password verified")
            if User.objects.filter(username=username).exists():
                messages.info(req,"username already exist")
                return redirect('User:Register')
            elif User.objects.filter(email=email).exists():
                messages.info(req,"email already exist")
                return redirect('User:Register')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                user.save()
                return redirect('User:Login')
        else:
            messages.info(req,"password not matched")
            return redirect('User:Register')
    return render(req, 'Register.html')

def login(req):
    if req.method=='POST':
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(req,user)
          print(user)
          req.session['user']=str(user)
          return redirect("mainapp:Home")
        else:
            messages.info(req, "invalidcredentials")
          
            return redirect('User:login')
    return render(req,'login.html')
def logout(req):
    auth.logout(req)
    req.session.pop('user',None)
    return redirect('mainapp:Home')