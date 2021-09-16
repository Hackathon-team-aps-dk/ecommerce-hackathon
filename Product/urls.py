from django.urls import path
from . views import create , query

urlpatterns = [
    path("create/" , create),
    path("query/" , query ,name = "query"),
]