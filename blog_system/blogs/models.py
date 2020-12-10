from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Blog(models.Model):
    slug = models.SlugField(
        editable=False,
    )
    name = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
