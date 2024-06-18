from django.urls import path
from staff.views import cust_data,shome,sbookings


urlpatterns=[
    path('',shome,name='shome'),
    path('cust_data/',cust_data,name='cust_data'),
    path('sbooking/',sbookings,name='sbooking'),
]