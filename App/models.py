from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=300)
    desc = models.TextField()

class donor(models.Model):
    name = models.CharField(max_length=122)
    product = models.CharField(max_length=122)
    mobile = models.TextField()
    location = models.CharField(max_length=122)
    quantity = models.CharField(max_length=122)
    about_product = models.TextField()

class login(models.Model):
    Username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    



def __str__(self):
    return self.name
