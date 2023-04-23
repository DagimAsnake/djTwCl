from twitter import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('tweet', views.tweet, name="tweet"),
    path('profile', views.profile, name="profile"),

]