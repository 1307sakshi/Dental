from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
from cust.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from cust.models import customer
from appoint.models import Appointment
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

@login_required
def custprofilepage(request):
    user_profile, created = customer.objects.get_or_create(user=request.user)
    user=request.user
    appointments = Appointment.objects.filter(user=request.user)
    cuser={
        'user':user,
        'appointments':appointments,
    }
    
    return render(request, 'cust/profilepage.html',cuser)


@login_required
def editprofile(request,id):
    if request.method == 'POST':
        sname=request.POST.get('name')
        smobile=request.POST.get('mobile')
        semail=request.POST.get('email')
        saddress=request.POST.get('address')
        sgender=request.POST.get('gender')
        
        sid=request.POST.get('id')
        if sid:
            store=customer.objects.get(id=sid)
            store.name=sname 
            store.mobile= smobile
            store.email=semail
            store.address=saddress
            store.gender=sgender
            
            store.save()
            
            return redirect('profilepage')
        
        else:
            pass
    s=customer.objects.get(pk=id)
    return render(request,'cust/editprofile.html',{'ser':s})





