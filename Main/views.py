from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from . forms import CreateNewList
from django.contrib.auth.models import User
from register.models import Profile

# Create your views here.
def home(response):
    username = None
    retail =False
    if response.user.is_authenticated:
        username = response.user.username
        users = list(Profile.objects.all())
        for user in users:
            if str(user) == str(username):
                retail = True
            else:
                retail = False
    return render(response , 'main/home.html' , {"retail":retail})

def start(response):
    return render(response , 'main/start.html')

def profile(response):
    username = None
    retail =False
    if response.user.is_authenticated:
        username = response.user.username
        users = list(Profile.objects.all())
        for user in users:
            if str(user) == str(username):
                retail = True
            else:
                retail = False
    return render(response , 'main/profile.html' , {'retail':retail , 'username':username , 'email':response.user.email})