from django.shortcuts import render
from services.models import service

# Create your views here.

def servic(request):
    ser = service.objects.all()
    return render(request, 'services/service.html',{'ser':ser})


