from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
# from userProfile import views
from users import views
class LoginMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response

    # def process_view(self,request,view_func,view_args,view_kwargs):
    #     if request.user:
    #         if (not request.user.is_authenticated):
    #             if(view_func)
    #             return redirect('login')