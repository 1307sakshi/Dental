from django.urls import path
from appoint.views import appointments,appointment_success,appointment_list,add,appointment_details


urlpatterns=[
    path('',appointments,name='appointment'),
    path('appointment_success',appointment_success, name='appointment_success'),
    path('mybookings/', appointment_list, name='mybookings'),
    path('book_service/<int:p_id>/',add, name='book_service'),
    path('appointment_details/<int:pk>/', appointment_details, name='appointment_details'),
]