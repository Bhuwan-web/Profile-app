from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()
class PostModel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post=models.TextField()
    posted_at=models.DateField(default=timezone.now)
    
