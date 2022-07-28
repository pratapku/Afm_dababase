from xml.etree.ElementInclude import default_loader
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import EmailField

from app.utils import create_new_ref_number, dt

class place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # field_id = models.ForeignKey(field, on_delete=models.CASCADE)
    place_id = models.CharField(max_length = 10,blank=False,unique=True,primary_key=True,default=create_new_ref_number)
    place_type = models.CharField(max_length=15)
    
class field(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
    place_id = models.ForeignKey(place, on_delete=models.CASCADE)
    field_id = models.CharField(max_length=10, blank=False, unique=True, primary_key=True, default=create_new_ref_number)

    field_name = models.CharField(max_length=15)
    def __str__(self):
      return self.field_name
class allDevices(models.Model):
    allDevices_id= models.CharField(max_length=40, default=0,primary_key=True)

class device(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    field_id = models.ForeignKey(field, on_delete=models.CASCADE)
    allDevices_id = models.OneToOneField(allDevices, on_delete=models.CASCADE)
    date_installed = models.DateField(default=dt)
    # def __str__(self):
    #   return self.field_id

class Device_status(models.Model):
    allDevices_id = models.OneToOneField(allDevices, on_delete=models.CASCADE,primary_key=True)
    pin2Status = models.IntegerField(blank=True,null=True,default=0)
    pin1Status = models.IntegerField(blank=True,null=True,default=0)
    pin3Status = models.IntegerField(blank=True,null=True,default=0)
    pin4Status = models.IntegerField(blank=True,null=True,default=0)
    pin5Status = models.IntegerField(blank=True,null=True,default=0)
    pin6Status = models.IntegerField(blank=True,null=True,default=0)
    pin7Status = models.IntegerField(blank=True,null=True,default=0)
    sensor1 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    sensor2 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    sensor3 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    sensor4 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    sensor5 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    sensor6 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    sensor7 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    # def __str__(self):
    #   return self.d_id

class Pin_name(models.Model):
    allDevices_id = models.OneToOneField(allDevices, on_delete=models.CASCADE,primary_key=True)
    pin1Name = models.CharField(blank=True,null=True,max_length=20)
    pin2Name = models.CharField(blank=True,null=True,max_length=20)
    pin3Name = models.CharField(blank=True,null=True,max_length=20)
    pin4Name = models.CharField(blank=True,null=True,max_length=20)
    pin5Name = models.CharField(blank=True,null=True,max_length=20)
    pin6Name = models.CharField(blank=True,null=True,max_length=20)
    pin7Name = models.CharField(blank=True,null=True,max_length=20)
    pin8Name = models.CharField(blank=True,null=True,max_length=20)
    pin9Name = models.CharField(blank=True,null=True,max_length=20)
   
    # def __str__(self):
    #   return self.d_id
   
class subuseraccess(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    emailtest = EmailField()
    email = models.CharField(primary_key=True, max_length=100)


class subuserplace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.ForeignKey(subuseraccess, on_delete=models.CASCADE,primary_key=True,unique=True)
    place_id = models.ForeignKey(place, on_delete=models.CASCADE,unique=True)

class tempuser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    email =models. EmailField(blank=True)
    name = models.CharField(max_length=100,blank=False)
    date = models.DateField(default="2000-01-01",null=True)
    timing = models.TimeField(default='00:00')
    place_id = models.ForeignKey(place, on_delete=models.CASCADE, blank=True, null=True)
    field_id = models.ForeignKey(field, on_delete=models.CASCADE, blank=True, null=True)
    device_id = models.ForeignKey(device, on_delete=models.CASCADE, blank=True, null=True)
    # r_id = models.ForeignKey(room, on_delete=models.CASCADE, blank=True, null=True)
    allDevices_id = models.ForeignKey(allDevices, on_delete=models.CASCADE, blank=True, null=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)