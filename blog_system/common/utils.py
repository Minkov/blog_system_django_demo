from blog_system.common.models import BlogSystemSettings


def can_user_create_blogs(user):
    settings = BlogSystemSettings.objects.first()
    return not user.is_authenticated or \
           user.blog_set.count() < settings.max_blogs_per_user
