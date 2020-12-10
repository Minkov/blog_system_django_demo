from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    display_name = models.CharField(max_length=30)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
