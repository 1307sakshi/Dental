from django.urls import path
from cust.views import home,about,contact,register,logins,logouts


urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('login/',logins,name='login'),
    path('logout/',logouts,name='logout'),
   
    
]