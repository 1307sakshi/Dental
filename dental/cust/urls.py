from django.urls import path
from cust.views import home,about,contact,register,logins,logouts,custprofilepage,editprofile


urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('login/',logins,name='login'),
    path('logout/',logouts,name='logout'),
    path('profilepage/',custprofilepage, name='profilepage'), 
    path('edit_profile/<int:id>/', editprofile, name='edit_profile'),
   
]