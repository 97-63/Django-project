from django.db import models

# Create your models here.
class Complain(models.Model):#here you are inheriting Model class present inside models package
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    subject=models.CharField(max_length=100)
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    complaintext=models.TextField()
class Career(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    qualification=models.CharField(max_length=50)
    experience=models.IntegerField()
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    cv=models.FileField(upload_to='cv/')
class LoginInfo(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
