from django import forms
from twitter.models import TweetList


class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetList
        fields = ['tweet']
