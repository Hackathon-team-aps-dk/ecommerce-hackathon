from django import template
from django.shortcuts import render
from django.template import Template
from django.contrib.auth.models import User

register = template.Library()

def idToUser(id):
    user = User.objects.get(id=int(id))
    return user

register.filter('idToUser', idToUser)