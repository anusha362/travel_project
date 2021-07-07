from django.db import models


# Create your models here.



class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class placedetails(models.Model):
    months=models.DateField(default=False)
    img=models.ImageField(upload_to='picture')
    heading=models.CharField(max_length=100)
    description=models.TextField()
