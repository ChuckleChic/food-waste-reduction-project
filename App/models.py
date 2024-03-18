from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()


class login(models.Model):
    name = models.CharField(max_length=122)
    product = models.CharField(max_length=122)
    mobile = models.TextField()
    location = models.CharField(max_length=200)
    quantity = models.CharField(max_length=122)
    about_product = models.TextField()


def __str__(self):
    return self.name
