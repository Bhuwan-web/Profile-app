from django.urls import path
from users import views
from users import api_views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api/login',api_views.LoginView,basename="api-login"),
# router.register('api/signup',api_views.SignupView,basename="api-signup"),
# app_name="users"
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    #users/
    path("login/",views.LoginUser.as_view(),name="login"),
    path("logout/",views.LogoutUser.as_view(),name="logout"),
    path("signup/",views.SignupView.as_view(),name="signup"),
    path("api/signup",api_views.SignupView.as_view(),name="api-signup"),

    # path("profile/",views.Profile.as_view(),name="profile"),
]

#for rest api urls
urlpatterns+=[
    path("rest/login",obtain_auth_token),



]


urlpatterns+=router.urls
