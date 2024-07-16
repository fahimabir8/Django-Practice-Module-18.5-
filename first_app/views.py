from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = RegistrationForm()
    return render(request,'login.html',{'form':form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request , data= request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass)
            
            if user is not None:
                login(request,user)
                messages.success(request, "Logged in successfully")
                return redirect('profile')
            
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.warning(request,"Logged out successfully !")
    return redirect('homepage')

def passchange(request):
    if request.method == "POST":
        form = SetPasswordForm(user = request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
        
    else:
        form = SetPasswordForm(user = request.user)
    return render(request, 'passchange.html', {'form' : form})

            
