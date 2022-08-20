from django.db import models

# Create your models here.


class Student(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Mobile = models.BigIntegerField()
    Email = models.EmailField()
    City = models.CharField(max_length=50)
