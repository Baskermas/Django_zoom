from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == "POST":
        return HttpResponse("<h2>{0}</h2>".format("There is the link."))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})