from django import template
from django.shortcuts import render
from django.template import Template
from django.contrib.auth.models import User
from Product.models import Product

register = template.Library()

def idToUser(id):
    user = User.objects.get(id=int(id))
    return user

def idToProduct(id):
    product = Product.objects.get(id=id)
    return product.id

register.filter('idToUser', idToUser)
register.filter('idToProduct', idToProduct)