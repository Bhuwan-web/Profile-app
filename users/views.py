
from userProfile.models import UserProfile
from django.contrib.auth.password_validation import validate_password
from django.http.response import HttpResponse
from django.views.generic import FormView
from users.forms import LoginForm, SignupForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model

# Create your views here.

User=get_user_model()
class LoginUser(LoginView):
    template_name='users/login.html'

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if not self.success_url:
            if bool(UserProfile.objects.get(login_infos__username=self.request.user).address):
                self.success_url="/"
            else:
             self.success_url='/userProfile/profile'
        return str(self.success_url)  # success_url may be lazy

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context["form"]=LoginForm
        return context

class LogoutUser(LogoutView):
    pass

    
class SignupView(FormView):
    template_name="users/signup.html"
    success_url='/users/login'
    form_class=SignupForm

    def cleaned_data(self,form,*args,**kwargs):
        username=form.cleaned_data['username']
        password=form.cleaned_data['password1']
        password2=form.cleaned_data['password2']
        if password==password2:
                user=User.objects.create(username=username)
                user.set_password(password)
                user.save()
                up=UserProfile.objects.create(login_infos_id=user.id)
                return self.form_valid(form)
        else:
            form=self.form_class()
            return HttpResponse("Invalid passwords")

    def post(self,request,*args,**kwargs):
        form=self.get_form()
        if form.is_valid():
            return self.cleaned_data(form)
        else:
            form=self.form_class()
            return HttpResponse("Invalid ")




