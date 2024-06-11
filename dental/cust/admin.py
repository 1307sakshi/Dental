from django.contrib import admin
from cust.models import customer

# Register your models here.

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display= ['created_at','name', 'mobile','email', 'address', 'gender']
    
# admin.site.register(customer, customerAdmin)

