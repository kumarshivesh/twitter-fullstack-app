from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  id_user = models.IntegerField()
  bio = models.TextField(blank=True)
  profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
  location = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return self.user.username

class Tweet(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField(max_length=240)
  photo = models.ImageField(upload_to='photos/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  no_of_likes = models.IntegerField(default=0)

  def __str__(self):
      return f'{self.user.username} - {self.text[:10]}'
  
class LikeTweet(models.Model):
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, default=1)  # Set an appropriate default value here
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username


