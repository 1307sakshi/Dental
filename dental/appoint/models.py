
from django.db import models
from django.contrib.auth.models import User



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
    
