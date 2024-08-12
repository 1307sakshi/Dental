from django.db import models

# Create your models here.
class service(models.Model):
    name= models.CharField( max_length=50)
    detail= models.TextField()
    price=models.CharField(max_length=50)
    piccture= models.FileField(upload_to='service/',null=True ,blank=True)