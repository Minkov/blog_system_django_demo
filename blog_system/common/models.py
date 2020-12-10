from django.db import models


class BlogSystemSettings(models.Model):
    max_blogs_per_user = models.IntegerField(
        default=3
    )
