from users.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class LoginSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=["username",'password']

class SignupSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password1=serializers.CharField(max_length=50,label="Password")
    password2=serializers.CharField(max_length=50,label="Confirm Password")
    # class Meta:
    #     model=User
    #     fileds=['username','password1','password2']
    