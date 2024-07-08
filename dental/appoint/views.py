
from django.shortcuts import render, redirect
from appoint.forms import AppointmentForm
from appoint.models import Appointment
from django.contrib.auth.decorators import login_required


@login_required
def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
    
        if form.is_valid():
            appointment=form.save()
            appointment.user = request.user
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/booking.html', {'form': form})


@login_required
def appointment_success(request):
    return render(request, 'appointment/success.html')  


@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointment/mybookings.html', {'appointments': appointments})
