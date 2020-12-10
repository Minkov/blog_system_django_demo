from django.contrib import admin
from .models import Blog, Post, Comment


class PostInline(admin.StackedInline):
    model = Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')

    inlines = (PostInline,)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post)
admin.site.register(Comment)
