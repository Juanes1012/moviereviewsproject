from django.shortcuts import render
from .models import Movie

def home(request):
    return render(request, "home.html", {"name": "Juan Esteban"})

def about(request):
    return render(request, "about.html")


