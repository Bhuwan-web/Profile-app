from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from userProfile.forms import ProfileDecoratorForm
from django.views.generic.base import TemplateView
from userProfile.models import AddressModel, BasicInfoModel, ProfileDecorator, UserProfile
from django.urls import reverse_lazy
from .forms import AddressForm, BasicInfoForm




class Profile(TemplateView):
    template_name="userProfile/profile.html"
    def get_context_data(self, **kwargs):
        user=UserProfile.objects.get(login_infos__username=self.request.user).__dict__
        context= super().get_context_data(**kwargs)
        context['user']=self.request.user
        try:
            context['address']=AddressModel.objects.get(id=user['address_id'])
        except:
            pass
        try:
            context["basic_info"]=BasicInfoModel.objects.get(id=user['basic_info_id'])
        except:
            pass
        
        try:
            context['profile']=ProfileDecorator.objects.get(id=user['profile_id'])
        except:
            pass
        return context

class ProfileDecoratorView(CreateView):
    #adding profile picture and bio for user profile
    queryset=ProfileDecorator.objects.all()
    template_name='userProfile/profile-decorator.html'
    form_class=ProfileDecoratorForm
    success_url=reverse_lazy("profile")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        user=UserProfile.objects.get(login_infos__username=self.request.user)
        user.profile_id=self.object.id
        user.save()
        return super().form_valid(form)

class ProfileDecoratorUpdateView(UpdateView):
    queryset=ProfileDecorator.objects.all()
    template_name='userProfile/profile-decorator.html'
    form_class=ProfileDecoratorForm
    success_url=reverse_lazy("profile")

class AddressView(CreateView):
    template_name="userProfile/address.html"
    success_url="/userProfile/profile"
    form_class=AddressForm
    fileds=['country','state','city','local']
    queryset=AddressModel.objects.all()

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        user=UserProfile.objects.get(login_infos__username=self.request.user)
        user.address_id=self.object.id
        user.save()
        return super().form_valid(form)

class AddressUpdate(UpdateView):
    template_name="userProfile/address.html"
    success_url="/userProfile/profile"
    form_class=AddressForm
    fileds=['country','state','city','local']
    queryset=AddressModel.objects.all()

class BasicInfoView(CreateView):
    template_name="userProfile/BasicInfo.html"
    success_url="/userProfile/profile"
    form_class=BasicInfoForm
    fileds=['first_name','last_name','age','sex','email']
    queryset=BasicInfoModel.objects.all()


    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        user=UserProfile.objects.get(login_infos__username=self.request.user)
        user.basic_info_id=self.object.id
        user.save()
        return super().form_valid(form)




    

