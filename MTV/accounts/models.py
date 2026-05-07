from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    studentnumber =models.CharField(max_length=7)
    major = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    



# Create your models here.
