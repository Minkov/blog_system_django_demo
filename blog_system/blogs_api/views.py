from rest_framework import generics as views
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from blog_system.blogs.models import Post, Blog


class PostSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ('title', 'text', 'blog_id')


class OwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class CreatePostApiView(views.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        blog = Blog.objects.get(pk=serializer.validated_data['blog_id'])
        if blog.user_id != self.request.user.id:
            raise PermissionDenied

        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
