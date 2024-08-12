from django.shortcuts import render, redirect,get_object_or_404
from cust.models import customer 
from django.contrib.auth.decorators import login_required
from appoint.models import Appointment,app
from services.models import service
# Create your views here.
def cust_data(request):
    s=customer.objects.all()
    
    return render(request,'staff/cust_data.html',{'cust':s})
def shome(request):
    return render(request,'staff/home.html')


def sbookings(request):
     if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        new_status = request.POST.get('status')
        appointment = get_object_or_404(app, id=appointment_id)
        appointment.status = new_status
        appointment.save()
        return redirect('sbooking')

    
     appointment = app.objects.all()
     return render(request, 'staff/sbooking.html',{'appointment':appointment}) 
    



def aserv(request):
    if request.method == 'POST':
        sname = request.POST.get('name')
        sdetail = request.POST.get('detail')
        sprice = request.POST.get('price')
        simage = request.FILES.get('piccture')
        
        if sname and sdetail and sprice and simage:
            service.objects.create(name=sname, detail=sdetail, price=sprice, piccture=simage)
    
    p = service.objects.all()
    return render(request, 'staff/aserv.html', {'serv': p})


def upserv(request, id):
    if request.method == 'POST':
        sname=request.POST.get('name')
        sdetail =request.POST.get('detail')
        sprice=request.POST.get('price')
        sid=request.POST.get('id')
        simage=request.POST.get('piccture')
        if sid:
            store=service.objects.get(id=sid)
            store.name=sname
            store.detail=sdetail
            store.price=sprice
            store.piccture=simage
            store.save()
            return redirect('/staff/aserv')
            
        else:
            pass

    z = service.objects.get(pk=id)
   
    return render(request,'staff/edit_serv.html',{'ser':z})

#to delete the service
def delserv(request, id):
    z = service.objects.filter(id=id)
    z.delete()
    return redirect('/staff/aserv')
    