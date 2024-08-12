from django.contrib import admin


from services.models import service


# Register your models here.
@admin.register(service)
class serviceAdmin(admin.ModelAdmin):
    list_display=['name','detail', 'price']