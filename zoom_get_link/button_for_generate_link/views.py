from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        return HttpResponse("<h2>{0}</h2>".format("There is the link."))
    else:
        return render(request, "index.html")