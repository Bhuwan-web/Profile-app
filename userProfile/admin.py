from django.contrib import admin
from .models import BasicInfoModel,ProfileDecorator,AddressModel,UserProfile
# Register your models here.
admin.site.register((BasicInfoModel,ProfileDecorator,AddressModel,UserProfile))