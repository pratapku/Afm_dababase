from rest_framework import serializers
from django.contrib.auth.models import User
# from drf_braces.serializers.form_serializer import FormSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


from .models import *
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

class userlogingetdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')
#
class placeSerializers(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = '__all__'

class placenameSerializers(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = ('place_type','place_id')
class subuserplacegetSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuserplace
        fields = ('name','email', 'place_id',)
#
class fieldSerializers(serializers.ModelSerializer):
    class Meta:
        model = field
        # fields = ('f_id', 'f_name')
        fields = '__all__'

class fieldnameSerializers(serializers.ModelSerializer):
    class Meta:
        model = field
        fields = ('field_name','field_id')
# class SerDevice(serializers.ModelSerializer):
#     class Meta:
#         model = device

#         fields = '__all__'
#         #
# class SerDeviceStatus(serializers.ModelSerializer):
#     class Meta:
#         model = Device_status
#         fields = '__all__'
class deviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = '__all__'



class deviceStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device_status
        fields = '__all__'
# class deviceStatusSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = deviceStatus
#         fields = '__all__'
        #




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
class tempuserregisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempuser
        fields= '__all__'
class dateasignSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempuser
        fields= ('id','date','timing',)
class timeasignSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempuser
        fields= ('timing',)

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
