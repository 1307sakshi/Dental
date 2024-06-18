from django.shortcuts import render, redirect,get_object_or_404
from cust.models import customer 
from django.contrib.auth.decorators import login_required
from appoint.models import Appointment

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
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.status = new_status
        appointment.save()
        return redirect('sbooking')

    
     appointment = Appointment.objects.all()
     return render(request, 'staff/sbooking.html',{'appointment':appointment}) 
    


    