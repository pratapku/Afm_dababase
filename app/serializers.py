from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from .models import *

class SerField(serializers.ModelSerializer):
    class Meta:
        model = field

        fields = '__all__'
class SerDevice(serializers.ModelSerializer):
    class Meta:
        model = device

        fields = '__all__'
        #
class SerDeviceStatus(serializers.ModelSerializer):
    class Meta:
        model = Device_status
        fields = '__all__'
        #
class SerPin_name(serializers.ModelSerializer):
    class Meta:
        model = Pin_name
        fields = '__all__'
class SerSubuseraccess(serializers.ModelSerializer):
    class Meta:
        model = subuseraccess
        fields = '__all__'
class SerPlace(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = '__all__'

class SerSubuserplace(serializers.ModelSerializer):
    class Meta:
        model = subuserplace
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 
          'first_name', 'last_name','email','password', 'password2')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
