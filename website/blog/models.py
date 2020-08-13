from django.db import models
from django.contrib.auth.models import User


class Tags(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to="images", default="/images/coding-final.png"
    )
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug =

    def __str__(self):
        return self.headline
