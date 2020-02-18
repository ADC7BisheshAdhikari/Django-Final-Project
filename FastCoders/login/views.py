from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
#Login
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        print("User object => ",user)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,"\"Username and password didn't match\"")
            return redirect('login')
    else:
        return render(request,'login.html')


#logout

def logout(request):
    auth.logout(request)
    return redirect('/')

# Signup
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"\"Username already registered\"")
                return render(request,'registerform.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"\"Email already registered\'")
                return render(request,'registerform.html')
            else:
             user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
             user.save()
             print('user created')
             return redirect('login')
             
        else:
            messages.info(request,'\"Password not matching\"')
            return render(request,'registerform.html')
        return render(request,'index.html')
    else:
        return render(request,'registerform.html')



