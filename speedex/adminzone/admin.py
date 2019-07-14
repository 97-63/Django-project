from django.contrib import admin
from .models import Notification,Quali,City,Packet
# Register your models here.
admin.site.register(Notification)
admin.site.register(Quali)
admin.site.register(City)
admin.site.register(Packet)