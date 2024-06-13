'''
from django.db import models

# Create your models here.

class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)


class ImageData(models.Model):
    Imagename=models.CharField(max_length=50)
    Image=models.ImageField(upload_to = "img/" )
    '''
from django.db import models  
  
# Create your models here.  
  
class Students(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    address = models.CharField(max_length=200)  
    roll_number = models.IntegerField()  
    mobile = models.CharField(max_length=10)  
  
    def __str__(self):  
        return self.first_name + " " + self.last_name  
