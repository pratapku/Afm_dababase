from django.http import HttpResponse
from django.shortcuts import render ,HttpResponse
from .serializers import SerDevice, SerDeviceStatus, SerField, SerPlace, SerPin_name, SerSubuseraccess, SerSubuserplace
from .models import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
# field
class Field(ListCreateAPIView):
    queryset = field.objects.all()
    serializer_class = SerField

class fieldRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = field.objects.all()
    serializer_class = SerField
    #device
class Device(ListCreateAPIView):
    queryset = device.objects.all()
    serializer_class = SerDevice
class deviceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = device.objects.all()
    serializer_class = SerDevice
    #deviceStatus
class DeviceStatus(ListCreateAPIView):
    queryset = Device_status.objects.all()
    serializer_class = SerDeviceStatus

class SerDeviceStatusRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Device_status.objects.all()
    serializer_class = SerDeviceStatus
    #
class pinname(ListCreateAPIView):
    queryset = Pin_name.objects.all()
    serializer_class = SerPin_name

class pinRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Pin_name.objects.all()
    serializer_class = SerPin_name
#
class Subuseraccess(ListCreateAPIView):
    queryset = subuseraccess.objects.all()
    serializer_class = SerSubuseraccess

class SubuseraccessRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = subuseraccess.objects.all()
    serializer_class = SerSubuseraccess
#
class Place(ListCreateAPIView):
    queryset = place.objects.all()
    serializer_class = SerPlace

class PlaceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = place.objects.all()
    serializer_class = SerPlace
#
class Subuserplace (ListCreateAPIView):
    queryset = subuserplace.objects.all()
    serializer_class = SerSubuserplace

class SubuserplaceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = subuserplace.objects.all()
    serializer_class = SerSubuserplace



def index(request):
    return HttpResponse("hello pK....")

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer





