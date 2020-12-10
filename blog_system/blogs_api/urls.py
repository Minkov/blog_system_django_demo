from django.urls import path

from blog_system.blogs_api.views import CreatePostApiView

urlpatterns = (
    path('', CreatePostApiView.as_view(), name='post create api'),
)
