from django.db.models import fields
from userProfile.models import AddressModel, BasicInfoModel, UserProfile
from rest_framework.serializers import ModelSerializer

class AddressSerilaizer(ModelSerializer):
    class Meta:
        model=AddressModel
        fields='__all__'

class BasicInfoSerializer(ModelSerializer):
        class Meta:
            model=BasicInfoModel
            fields='__all__'    

class UserProfileSerializer(ModelSerializer):
    basic_info=BasicInfoSerializer()
    address=AddressSerilaizer
    class Meta:
        model=UserProfile
        fields='__all__'