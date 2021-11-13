from rest_framework.serializers import ModelSerializer
from .models import PostModel
class PostSerializer(ModelSerializer):
    # author=forms.CharField(max_length=50)
    class Meta:
        model=PostModel
        fields=['post','author','posted_at']

# class CreatePostForm(Serializer):
#     # author=forms.CharField(max_length=50)
#     class Meta:
#         model=PostModel
#         fields=['post',]
#         # order_by="-id"