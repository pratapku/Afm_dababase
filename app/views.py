import json
from django.http import HttpResponse
from django.shortcuts import render ,HttpResponse

from app.utils import get_variable
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
from rest_framework.decorators import api_view

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def useridList(request):
    if request.method=="GET":
        current_user = request.user
        print(current_user.id)
        return Response(current_user.id)
################place##########
 
                                      
@api_view(["GET","POST","PUT","DELETE"])
# @permission_classes([IsAuthenticated])
def placeList(request):
    if request.method=="GET":
        data = place.objects.filter(user=request.user)
        placeJson = placeSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)
        # dd = placeJson.data[:]
        # return Response(dd[0])
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = placeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(get_variable(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['place_id']
        try:
            device_object=place.objects.get(place_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = placeSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        data = place.objects.filter(p_id=request.GET['place_id'])
        # data2 = subuseraccess.objects.filter(email=request.GET['email'])
        # placeJson = subuserplaceSerializers(data, many=True)
        data.delete()
        # data2.delete()
        return Response("removed")

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def placegetList(request):
    if request.method=="GET":
        data = place.objects.filter(user = request.user)
        placeJson = placeSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)

           ################### Without security ###################################

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def placegetallList(request):
    if request.method=="GET":
        data = subuserplace.objects.filter(email=request.GET['email'])
        placeJson = subuserplacegetSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)

# field

@api_view(["GET", "POST","PUT","DELETE"])
def fieldList(request):
    if request.method=="GET":
        floor_data = field.objects.filter(user = request.user,place_id=request.GET['place_id'])
        floorJson = fieldSerializers(floor_data, many=True)
        # dd = floorJson.data[:]
        return Response(floorJson.data)

    
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = fieldSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(get_variable(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        received_json_data=json.loads(request.body)
        device_id=received_json_data['field_id']
        try:
            device_object=field.objects.get(field_id=device_id)
        except device_object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = fieldSerializers(device_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data updated", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        data = field.objects.filter(field_id=request.GET['field_id'])
        # data2 = subuseraccess.objects.filter(email=request.GET['email'])
        # placeJson = subuserplaceSerializers(data, many=True)
        data.delete()
        # data2.delete()
        return Response("removed")

@api_view(["GET"])
def fieldgetList(request):
    if request.method=="GET":
        floor_data = field.objects.filter(user = request.user,place_id=request.GET['place_id'])
        floorJson = fieldSerializers(floor_data, many=True)
        return Response(floorJson.data)

                ################### Without security ###################################

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def fieldgetallList(request):
    if request.method=="GET":
        data = field.objects.filter(place_id=request.GET['place_id'])
        placeJson = fieldSerializers(data, many=True)
        print(data)
        return Response(placeJson.data)

# class Field(ListCreateAPIView):
#     queryset = field.objects.all()
#     serializer_class = SerField

# class fieldRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = field.objects.all()
#     serializer_class = SerField
    #device
# class Device(ListCreateAPIView):
#     queryset = device.objects.all()
#     serializer_class = SerDevice
# class deviceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = device.objects.all()
#     serializer_class = SerDevice
#     #deviceStatus
# class DeviceStatus(ListCreateAPIView):
#     queryset = Device_status.objects.all()
#     serializer_class = SerDeviceStatus

@api_view(["GET","POST","DELETE"])
def deviceList(request):
    if request.method=="GET":
        field_id = device.objects.filter(user = request.user,field_id=request.GET['field_id'])
        fieldJson = deviceSerializers(field_id, many=True)
        # rr = roomJson.data[:]
        return Response(fieldJson.data)
    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        serializer = deviceSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        data = device.objects.filter(field_id=request.GET['field_id'], allDevices_id=request.GET['allDevices_id'])
        # data2 = subuseraccess.objects.filter(email=request.GET['email'])
        # placeJson = subuserplaceSerializers(data, many=True)
        data.delete()
        # data2.delete()
        return Response("removed")

@api_view(["GET"])
def devicegetList(request):
    if request.method=="GET":
        field_data = device.objects.filter(user = request.user,field_id=request.GET['field_id'])
        devJson = deviceSerializers(field_data, many=True)
        return Response(devJson.data)


                ################### Without security ###################################

@api_view(["GET"])
def devicegetallList(request):
    if request.method=="GET":
        field_data = device.objects.filter(field_id=request.GET['field_id'])
        devJson = deviceSerializers (field_data, many=True)
        return Response(devJson.data)

# class SerDeviceStatusRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Device_status.objects.all()
#     serializer_class = SerDeviceStatus
    #

@api_view(["GET","POST"])
def devicePinStatus(request):
    if request.method == "GET":
        device_data = Device_status.objects.filter(allDevices_id=request.GET['allDevices_id'])
        roomJson = deviceStatusSerializers(device_data, many=True)
        dd = roomJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        if received_json_data['put']!='yes':
            serializer = deviceStatusSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data created", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            device_id=received_json_data['allDevices_id']
            print('123')
            try:
                print('qwe')
                device_object=Device_status.objects.get(allDevices_id=device_id)
            except device_object.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = deviceStatusSerializers(device_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data updated", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#
@api_view(["GET","POST"])
def devicePinName(request):
    if request.method == "GET":
        device_data = Pin_name.objects.filter(allDevices_id=request.GET['allDevices_id'])
        roomJson = SerPin_name(device_data, many=True)
        dd = roomJson.data[:]
        return Response(dd[0])

    elif request.method == "POST":
        received_json_data=json.loads(request.body)
        if received_json_data['put']!='yes':
            serializer = SerPin_name(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data created", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            device_id=received_json_data['allDevices_id']
            print('123')
            try:
                print('qwe')
                device_object=Pin_name.objects.get(allDevices_id=device_id)
            except device_object.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SerPin_name(device_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("data updated", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    ####
@api_view(["GET"])
def tempulist(request):
    if request.method == "GET":
        device_data = tempuser.objects.filter(user=request.user)
        nameJson = tempuserregisterSerializers(device_data, many=True)
        return Response(nameJson.data)
@api_view(["GET","POST","DELETE"])
def tempU(request):
    if request.method == "GET":
        device_data = tempuser.objects.filter(mobile=request.GET['mobile'])
        nameJson = tempuserregisterSerializers(device_data, many=True)
        return Response(nameJson.data)
    elif request.method == "POST":
        tempdata = tempuserregisterSerializers(data=request.data)
        if tempdata.is_valid():
            tempdata.save()
            return Response("Temporary User is now active.", status=status.HTTP_201_CREATED)
        return Response(tempdata.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # received_json_data=json.loads(request.body)
        # if received_json_data['id']=='p_id':
        try:
            data = tempuser.objects.filter(mobile=request.GET['mobile'], place_id=request.GET['place_id'])
            #print(data)
            data.delete()
        except Exception:
            print("place_id not found")
            pass

        try:
        # elif received_json_data['id']=='f_id':
            data2 = tempuser.objects.filter(mobile=request.GET['mobile'], field_id=request.GET['field_id'])
            data2.delete()
        except Exception:
            print("field_id not found")
            pass
        # elif received_json_data['id']=='r_id':

        try:
            data3 = tempuser.objects.filter(mobile=request.GET['mobile'], allDevices_id=request.GET['allDevices_id'])
            data3.delete()
        
        # elif received_json_data['id']=='d_id':
        except Exception:
            print("allDevices_id not found")
            pass
        try:
            data4 = tempuser.objects.filter(mobile=request.GET['mobile'], device_id=request.GET['device_id'])
            data4.delete()
        except Exception:
            print("device_id not found")
            pass

        # else:
        #     print("not found")
        # data2 = tempUserVerification.objects.filter(mobile=request.GET['mobile']) or tempUserVerification.objects.filter(email=request.GET['email'])
        # data3 = otptemplogin.objects.filter(mobile=request.GET['mobile']) or otptemplogin.objects.filter(email=request.GET['email'])
        # data2.delete()
        # data3.delete()
        return Response("Temporary User has no longer Exists.")

#######indeex##########

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





