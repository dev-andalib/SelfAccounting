from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate


def home(request):
    return render(request, 'home.html', home)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if authenticate(username = username, password = password) != None:
                return redirect(home) 
            
            else:
                form.add_error(None, 'Invalid login credentials')
                
        else:
            form.add_error(None, 'Please correct the errors below')        
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})



def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("login") 
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})