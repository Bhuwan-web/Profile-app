from post.forms import CreatePostForm, PostForm
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import PostModel
from userProfile.models import UserProfile
from django.core.paginator import Paginator
# Create your views here.
class PostView(ListView):
    queryset=PostModel.objects.all().order_by('-id')
    template_name='post/home.html'
    context_object_name="posts"
    paginate_by=5
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        # context['form'] = self.get_form()
        try:
            context['profile']=UserProfile.objects.get(login_infos__username=self.request.user)
        except:
            context['profile']="Anon"
        return context

class CreatePostView(CreateView,PostView):
    form_class=CreatePostForm
    fileds=('post',)
    template_name='post/home.html'
    success_url='/'

    def form_valid(self, form):
        self.object=form.save()
        try:
            self.object.author=self.request.user
        except:
            pass
        self.object.save()
        return super().form_valid(form)

