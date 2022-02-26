from ast import mod
from re import M
from django.db import models

# Create your models here.

class Patient(models.Model):


    name = models.CharField(max_length=20)
    age = models.CharField(max_length=2)

    gen = (
        ('M','Male'),
        ('F','Female'),
        ('T','Other'),

    )

    mobile = models.CharField(max_length=10)
    gender = models.CharField(choices=gen,max_length=3)

    address = models.TextField()

    def __str__(self):
        return self.name

    