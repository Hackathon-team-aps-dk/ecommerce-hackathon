from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import ToDoList , Item
from . forms import CreateNewList

# Create your views here.
def index(response , id):
    listName = ToDoList.objects.get(id=id)
    return render(response , 'main/base.html' , {"name":listName})

def home(response):
    return render(response , 'main/home.html' , {"name":"test"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            response.user.todolist.create(name=name)
            
    else:
        form = CreateNewList()
    return render(response , 'main/test.html' , {"form": form})

def start(response):
    return render(response , 'main/start.html')