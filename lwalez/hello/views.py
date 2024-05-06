from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#A view is something that a user may want to see
#This fn takes a request that a user made to access our web server i.e GET or POST request as argument
def index(request):
    return render(request, "hello/index.html")

def cecil(request):
    return HttpResponse("Hello, Joel!!!")

def greet(request, name):
    return render(request, "hello/index.html", {
        "name" : name.capitalize()
    })
