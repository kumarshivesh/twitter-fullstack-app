from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  profileimg = forms.ImageField(required=False)
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'profileimg')

class TweetForm(forms.ModelForm):
  class Meta:
    model = Tweet
    fields = ['text', 'photo']
