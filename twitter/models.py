from django.db import models

# Create your models here.


class TweetList(models.Model):
    tweet = models.CharField(max_length=100)

    def __str__(self):
        return self.tweet
