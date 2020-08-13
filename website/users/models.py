from django.db import models
from django.contrib.auth.models import User


class Learner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # points =

    def __str__(self):
        return self.name
