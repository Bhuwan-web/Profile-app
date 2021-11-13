from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING
# Create your models here.
User=get_user_model()

class BasicInfoModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'basic_model: {self.first_name} {self.last_name}'

class ProfileDecorator(models.Model):
    profile_pic=models.FileField(upload_to='images/',null=True,blank=True)
    bio=models.CharField(max_length=150)

class AddressModel(models.Model):
    country = models.CharField(max_length=50, default="Nepal")
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    local = models.CharField(max_length=50)


class UserProfile(models.Model):
    basic_info = models.ForeignKey(BasicInfoModel, on_delete=models.DO_NOTHING,null=True)
    profile=models.OneToOneField(ProfileDecorator,on_delete=DO_NOTHING,null=True)
    address = models.ForeignKey(AddressModel, on_delete=models.DO_NOTHING,null=True)
    login_infos=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
