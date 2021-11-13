from post.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from .models import PostModel
from userProfile.models import UserProfile


class ApiPostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset=PostModel.objects.all()
    

