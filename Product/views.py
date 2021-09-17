from django.shortcuts import render , redirect
from register import models
from . forms import CreateNewProduct
from . models import Product

# Create your views here.
def create(response):
    if response.method == "POST":
        form = CreateNewProduct(response.POST)
        if form.is_valid():
            form.instance.poster = response.user
            form.save()
            return redirect('/home')
    else:
        form = CreateNewProduct()
    username = None
    retail =False
    if response.user.is_authenticated:
        username = response.user.username
        users = list(models.Profile.objects.filter(Retailer = True))
        for user in users:
            if str(user) == str(username):
                retail = True
            else:
                retail = False
    return render (response , 'product/sell.html' , {'retail':retail , 'form':form})

def query(response):
    username = None
    retail =False
    if response.user.is_authenticated:
        username = response.user.username
        users = list(models.Profile.objects.filter(Retailer = True))
        for user in users:
            if str(user) == str(username):
                retail = True
            else:
                retail = False
    if response.method == 'GET':
        search = response.GET.get("search")
        products = list(Product.objects.filter(productName__icontains=f'{search}').values())
    return render(response , 'main/home.html' , {"retail":retail , 'products':products})

    