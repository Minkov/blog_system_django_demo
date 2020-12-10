from django import template

from blog_system.common.utils import can_user_create_blogs

register = template.Library()


@register.inclusion_tag('partials/create_blog.html')
def create_blog(user):
    return {
        'disabled': not can_user_create_blogs(user),
    }
