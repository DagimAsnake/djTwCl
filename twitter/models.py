from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TweetList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    tweet = models.CharField(max_length=100)

    def __str__(self):
        return self.tweet
