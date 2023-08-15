from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    from_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.from_user.user.username}"
