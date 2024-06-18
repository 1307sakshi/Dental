
from django.shortcuts import render, redirect
from appoint.forms import AppointmentForm
from appoint.models import Appointment


def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/booking.html', {'form': form})



def appointment_success(request):
    return render(request, 'appointment/success.html')  



def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment/mybookings.html', {'appointments': appointments})
