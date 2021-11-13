from users import urls
from django.urls import path
from django.views.generic.edit import CreateView
from .views import CreatePostView, PostView
from rest_framework.routers import DefaultRouter
from . import api_views
router=DefaultRouter()
router.register("api/posts",api_views.ApiPostView,basename='apipost')


urlpatterns = [
    # path("",PostView.as_view(),name="home"),
    path("",CreatePostView.as_view(),name='home')
]
urlpatterns+=router.urls
