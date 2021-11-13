from django.contrib.auth.mixins import LoginRequiredMixin


class LoginMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response