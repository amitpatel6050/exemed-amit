from django.db import models
from random import choices
from secrets import choice
from turtle import position
from django.db import models
from django.utils import timezone



# Create your models here.

class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    mobile=models.PositiveIntegerField()
    Desc = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name+" "+self.company+" "+self.city+" "+self.Desc
    

class Employee_reg(models.Model):
    name = models.CharField(max_length=100)
    cp = models.CharField(max_length=100)
    ce = models.CharField(max_length=100)
    dp = models.CharField(max_length=100)
    email = models.EmailField()
    mobile=models.PositiveIntegerField()
    resume = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name+" "+self.cp+" "+self.ce+" "+self.dp