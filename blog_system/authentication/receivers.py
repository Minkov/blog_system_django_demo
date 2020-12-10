from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog_system.authentication.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile(
            user=instance,
            display_name=instance.username
        )
        profile.save()
