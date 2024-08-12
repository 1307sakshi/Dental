from django.urls import path

from services.views import servic

urlpatterns = [
    path('',servic, name='service'),

  
]
