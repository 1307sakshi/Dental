from django.urls import path
from staff.views import cust_data,shome,sbookings,aserv,upserv,delserv


urlpatterns=[
    path('',shome,name='shome'),
    path('cust_data/',cust_data,name='cust_data'),
    path('sbooking/',sbookings,name='sbooking'),
    path('aserv/',aserv,name='aserv'),
    path('update/<int:id>',upserv,name='upserv'),#url for updateing the service 
    path('dels/<int:id>',delserv,name='delserv'),#url for deleting the service 
]