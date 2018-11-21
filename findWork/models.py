
from django.db import models,connection
class User(models.Model):
    FirstName =models.CharField(max_length=30)
    LastName =models.CharField(max_length=30)
    Username =models.CharField(max_length=30)
    Password =models.CharField(max_length=30)
    Phone   =models.IntegerField()

class Administrator(models.Model):
    FirstName =models.CharField(max_length=30)
    LastName =models.CharField(max_length=30)
    Username =models.CharField(max_length=30)
    Password =models.CharField(max_length=30)

class Payment(models.Model):
    Type =models.CharField(max_length=30)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

class Works(models.Model):
    Description =models.CharField(max_length=30)
    Type =models.CharField(max_length=30)
    StartDate =models.DateField(auto_now=False, auto_now_add=False)
    Finaldate =models.DateField(auto_now=False, auto_now_add=False)
    Price=models.IntegerField()
    UserBoss = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Boss')
    UserEmployee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Employee')
    Address=models.CharField(max_length=30)

class applicant(models.Model):
    UserBoss1 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Boss1')
    UserEmployee1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Employee1')
    WorkID= models.ForeignKey(Works, on_delete=models.CASCADE,related_name='WorkID')
