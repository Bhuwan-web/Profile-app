from django.http import request
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #userProfile
    path("profile",views.Profile.as_view(),name="profile"),
    # path("profile-list",views.ProfileList.as_view(),name="profile"),
    path("profile-decorator/",views.ProfileDecoratorView.as_view(),name="profile-decorator"),
    path("profile-decorator/<int:pk>",views.ProfileDecoratorUpdateView.as_view(),name="profile-decorator-update"),

    path("address/",views.AddressView.as_view(),name="address"),
    path("address/<int:pk>",views.AddressUpdate.as_view(),name="address-update"),

    path("basic-info/",views.BasicInfoView.as_view(),name="basic-info"),



]
