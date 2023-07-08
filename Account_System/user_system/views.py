from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model





def home(request):
    # context={}
    # context.update(newcontext)
    #return render(request,"user_system/index.html",context)
    return render(request, "user_system/index.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pass1']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'user_system/index.html',{'fname':fname})
            # return redirect(reverse('home',kwargs={'fname':fname}))
        else:
            messages.error(request,"Please Enter Valid Credentials")
            return redirect('signin')
    return render(request,"user_system/signin.html")


def signup(request):
    User = get_user_model()
    if request.method == "POST":
        fullname = request.POST['fname']
        username = request.POST['uname']
        emailid = request.POST['email']
        phoneno = request.POST['phoneno']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']


        myuser = User.objects.create_user(first_name=fullname,last_name=phoneno,username=username,email= emailid,password=password1,password2=password2)
        myuser.save()

        messages.success(request, "Account Successfully created. We have send you mail to activate your Account please Confirm ")
        return redirect('signin')
    return render(request,"user_system/signup.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')