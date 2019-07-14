from django.db import models

# Create your models here.
class Notification(models.Model):
    notificationmsg=models.TextField()
    posteddate=models.CharField(max_length=20)

class City(models.Model):
    cityname = models.CharField(max_length=100)

class Packet(models.Model):
    refno=models.CharField(max_length=20,primary_key=True)
    sendername=models.CharField(max_length=50)
    senderaddress=models.TextField()
    sendermobno=models.CharField(max_length=15)#because '+' is also there in a  mobile nno.
    receivername=models.CharField(max_length=50)
    receiveraddress=models.TextField()
    receivermobno=models.CharField(max_length=15)
    source=models.CharField(max_length=50)#senders city name
    mid=models.CharField(max_length=50)#intermediates cities
    destination=models.CharField(max_length=50)#recivers city name
    weight=models.CharField(max_length=10)#packet weight its charfield so that grams kg is also accomodated
    charge=models.IntegerField()
    posteddate=models.CharField(max_length=30)
    status=models.CharField(max_length=10)#status of packet can be inititated,pending,delivered

class Quali(models.Model):
    applicantquali=models.CharField(max_length=10)





