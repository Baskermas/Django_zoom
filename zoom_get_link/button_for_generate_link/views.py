from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        return HttpResponse("<h2>Hello, {0}</h2>".format('There is the Link'))