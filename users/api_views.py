from rest_framework.serializers import Serializer
from userProfile.models import UserProfile
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from users import serializers
from users.models import User
from users.serializers import LoginSerializer, SignupSerializer
from rest_framework.viewsets import ModelViewSet


class LoginView(ModelViewSet):
    serializer_class=LoginSerializer
    queryset=User.objects.all()

class SignupView(CreateAPIView):
    serializer_class=SignupSerializer
    queryset=User.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid=serializer.validated_data
        username=valid['username']
        password1=valid['password1']
        password2=valid['password2']
        if password1==password2:
            user=User.objects.create(username=username,password=password1)
            user.set_password(password1)
            user.save()
            UserProfile.objects.create(login_infos_id=user.id)
        else:
            return Response({"error":"Password mismatched"},status=status.HTTP_400_BAD_REQUEST)
        # self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()

