from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('blog_system.authentication.urls')),
    path('', include('blog_system.blogs.urls')),
    path('api/blogs/', include('blog_system.blogs_api.urls')),
]