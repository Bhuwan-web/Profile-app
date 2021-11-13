from django import forms
from django.db import models
from django.db.models import fields
from .models import AddressModel,BasicInfoModel, ProfileDecorator,UserProfile

class AddressForm(forms.ModelForm):
    class Meta:
        model=AddressModel
        fields='__all__'

class BasicInfoForm(forms.ModelForm):
        class Meta:
            model=BasicInfoModel
            fields='__all__'    

class UserProfileForm(forms.ModelForm):
    basic_info=BasicInfoForm
    address=AddressForm
    class Meta:
        model=UserProfile
        fields='__all__'

class ProfileDecoratorForm(forms.ModelForm):
    class Meta:
        model=ProfileDecorator
        fields='__all__'