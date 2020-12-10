from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from blog_system.blogs.models import Blog
from blog_system.common.utils import can_user_create_blogs


class BlogsListView(views.ListView):
    template_name = 'blogs/list.html'
    model = Blog


class BlogDetailsView(views.DetailView):
    template_name = 'blogs/details.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = self.get_object().post_set.all()

        return context


class CreateBlogView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Blog
    template_name = 'blogs/create.html'
    fields = ('name', 'description')

    def dispatch(self, request, *args, **kwargs):
        if not can_user_create_blogs(request.user):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
