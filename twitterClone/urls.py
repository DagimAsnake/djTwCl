from django.contrib import admin
from django.urls import path, include
from twitter import views as twitterViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('twitter/', include('twitter.urls')),
    path('', twitterViews.index, name='index')
]
