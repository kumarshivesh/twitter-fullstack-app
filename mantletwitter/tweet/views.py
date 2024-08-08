from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Tweet
from .forms import UserRegistrationForm, TweetForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
  return  render(request, 'index.html')

def tweet_list(reqest):
  tweets = Tweet.objects.all().order_by('-created_at')
  return render(reqest, 'tweet_list.html', {'tweets': tweets})


def signup(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save(commit=False)
      user.first_name = form.cleaned_data.get('first_name')
      user.last_name = form.cleaned_data.get('last_name')
      user.save()
      
      profileimg = form.cleaned_data.get('profileimg') or 'profile_images/blank-profile-picture.png'
      
      # Create a Profile object for the new user
      Profile.objects.create(user=user, id_user=user.id, profileimg=profileimg)
      
      # Log the user in and redirect to 'tweet_list' page 
      user_login = auth.authenticate(username=user.username, password=form.cleaned_data.get('password1'))
      auth.login(request, user_login)
      
      return redirect('tweet_list')
    else:
      messages.error(request, form.errors)
      return redirect('signup')
  else:
    form = UserRegistrationForm()
  return render(request, 'registration/signup.html', {'form': form})

def custom_logout(request):
  logout(request)
  return redirect('tweet_list') # Redirect to 'tweet_list' (temporarily to 'index' page)

@login_required
def tweet_create(request):
  if request.method == "POST":
   form = TweetForm(request.POST, request.FILES)
   if form.is_valid():
     tweet = form.save(commit=False)
     tweet.user = request.user
     tweet.save()
     return redirect('tweet_list')
  else:
    form = TweetForm()
  return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
  tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
  if request.method == "POST":
   form = TweetForm(request.POST, request.FILES, instance=tweet)
   if form.is_valid():
     tweet = form.save(commit=False)
     tweet.user = request.user
     tweet.save()
     return redirect('tweet_list')
  else:
    form = TweetForm(instance=tweet)
  return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
  tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
  if request.method == "POST":
    tweet.delete()
    return redirect('tweet_list')
  return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def search(request):
  query = request.GET.get('q')
  if query:
    results = Tweet.objects.filter(text__icontains=query)
  else:
    results = Tweet.objects.none()
  return render(request, 'search_results.html', {'results': results, 'query': query})

