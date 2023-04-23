from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tweet(request):
    context= {
        "tweet": "Tweets page"
    }
    return render((request), 'tweet.html', context)

def home(request):
    context= {
        "home": "Home page"
    }
    return render((request), 'home.html', context)

def profile(request):
    context= {
        "profile": "Profile page"
    }
    return render((request), 'profile.html', context)