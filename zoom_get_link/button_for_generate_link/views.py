from django.shortcuts import render
from django.http import HttpResponse
import re
from button_for_generate_link import create_the_link



def index(request):
    if request.method == "POST":
        gen_link = create_the_link.createMeeting()
        gen_link = re.findall(r"https.*?\s", gen_link)
        link = gen_link[0]
        return HttpResponse("<h2>The link is: {0}</h2>".format(link))
    else:
        return render(request, "index.html")