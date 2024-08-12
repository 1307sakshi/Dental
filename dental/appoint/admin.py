from django.contrib import admin
from appoint.models import Appointment
from appoint.models import app, appitem
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display= ['user','name','email', 'phone','date', 'time', 'message','status']


# Register your models here.

@admin.register(app)
class appAdmin(admin.ModelAdmin):
    list_display= [ 'user','created_at','total_amount']
    
@admin.register(appitem)
class appitemAdmin(admin.ModelAdmin):
    list_display= [ 'app','app_service']   

