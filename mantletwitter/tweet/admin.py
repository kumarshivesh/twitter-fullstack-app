from django.contrib import admin
from .models import Profile, Tweet, LikeTweet, Favorite

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tweet)
admin.site.register(LikeTweet)
admin.site.register(Favorite)