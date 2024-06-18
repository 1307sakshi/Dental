from django.contrib import admin
from appoint.models import Appointment

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display= ['name','email', 'phone','date', 'time', 'message','status']
    

