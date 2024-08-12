
from django.shortcuts import render, redirect,get_object_or_404
from appoint.forms import AppointmentForm,CheckoutForm
from appoint.models import Appointment,app,appitem
from django.contrib.auth.decorators import login_required 
from services.models import service

@login_required
def appointments(request):
    user=request.user
    if user.is_authenticated:
        apps = app.objects.filter(user=request.user, finalized=False).last()
        if apps:
            appitems = apps.appitem_set.all()
            totalprice = sum(float(item.app_service.price) for item in appitems)
        else:
            appitems = []
            totalprice = 0

        if request.method == 'POST':
            form = CheckoutForm(request.POST)
            if form.is_valid():
                appointment = form.save(commit=False)
                appointment.user = request.user
                appointment.total_amount = totalprice
                appointment.finalized = True
                appointment.save()
                for item in appitems:
                    item.app = appointment
                    item.save()
                return redirect('appointment_details', pk=appointment.pk)
        else:
            form = CheckoutForm()

        return render(request, 'appointment/booking.html', {'appitems': appitems, 'totalprice': totalprice, 'form': form})
    return redirect('login')


@login_required
def appointment_success(request):
    return render(request, 'appointment/success.html')  


@login_required
def appointment_list(request):
    appointments = app.objects.filter(user=request.user)
    return render(request, 'appointment/mybookings.html', {'appointments': appointments})

def add(request,p_id):
    user=request.user
    if user.is_authenticated:
        ser = get_object_or_404(service, pk=p_id)
        apps, created = app.objects.get_or_create(user=request.user, finalized=False)
        app_item, created = appitem.objects.get_or_create(app=apps, app_service=ser)

        if not created:
            app_item.save()

        #apps.total_amount += Decimal(ser.price)
        apps.save()

        return redirect('appointment')
    return redirect('login')

def appointment_details(request, pk):
    appointment = app.objects.get(pk=pk)
    appitems = appointment.appitem_set.all()
    return render(request, 'appointment/appoint_details.html', {'appointment': appointment,'appitems': appitems})