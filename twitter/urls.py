from twitter import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('tweet', views.tweet, name="tweet"),
    path('profile', views.mytweets, name="profile"),
    path('delete/<tweetId>', views.deleteTweet, name="deleteTweet"),
    path('user/<userId>', views.userTweet, name='userTweet')
]
