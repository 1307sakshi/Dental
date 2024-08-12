
from django.db import models
from django.contrib.auth.models import User
from services.models import service


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')


    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'
    




class app(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    app_service=models.ManyToManyField(service, through='appitem')
    created_at= models.DateTimeField(auto_now_add=True,null=True)
    total_amount=models.DecimalField(max_digits=7,decimal_places=2,null=True)
  
    preferred_date = models.DateField(null=True)
    message = models.TextField(blank=True, null=True)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    
    
    
    def _str_(self):
        return self.user.username
    
class appitem(models.Model):
     app=models.ForeignKey(app, on_delete=models.CASCADE,null=True)
     app_service=models.ForeignKey(service, on_delete=models.CASCADE,null=True)
     
     def _str_(self):
        return self.app.user.username