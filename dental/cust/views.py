from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
from cust.forms import RegisterForm


# Create your views here.
def home(request):
    return render(request,'cust/home.html')
def about(request):
    return render(request,'cust/about.html')
def contact(request):
    return render(request,'cust/contacts.html')

def logins(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,('Login Sucessful!!!'))
            return redirect('home')
        
        else:
            messages.success(request,('Login UNSucessful!!!'))
            return redirect('login')
    return render(request,'cust/login.html')


def logouts(request):
    logout(request)
    messages.success(request,("You've loged out sucessfully"))
    return redirect('home')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a page after successful registration
    else:
        form = RegisterForm()
    return render(request,'cust/register.html', {'form': form})



