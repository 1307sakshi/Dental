from django.urls import path
from appoint.views import appointments,appointment_success,appointment_list


urlpatterns=[
    path('',appointments,name='appointment'),
    path('appointment_success',appointment_success, name='appointment_success'),
    path('mybookings/', appointment_list, name='mybookings'),
]