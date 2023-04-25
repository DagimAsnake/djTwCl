from django.shortcuts import render, redirect
from django.http import HttpResponse
from twitter.models import TweetList
from twitter.forms import TweetForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request, ('You Added New Tweet!'))
        return redirect('/twitter')
    else:
        return render((request), 'tweet.html', {})


def home(request):
    allTweets = TweetList.objects.all()
    paginator = Paginator(allTweets, 5)
    page = request.GET.get('pg')
    allTweets = paginator.get_page(page)
    return render((request), 'home.html', {"allTweets": allTweets})

@login_required
def profile(request):
    context = {
        "profile": "Profile page"
    }
    return render((request), 'profile.html', context)

@login_required
def mytweets(request):
    myTweets = TweetList.objects.filter(manage=request.user)
    paginator = Paginator(myTweets, 5)
    page = request.GET.get('pg')
    myTweets = paginator.get_page(page)
    return render((request), 'mytweets.html', {"myTweets": myTweets})

@login_required
def deleteTweet(request, tweetId):
    tweet = TweetList.objects.get(pk=tweetId)
    tweet.delete()
    return redirect('/twitter/profile/mytweets')


def index(request):
    context = {
        "index": "index page"
    }
    return render((request), 'index.html', context)
