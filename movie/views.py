from django.shortcuts import render
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {
        "movies": movies,
        "name": "Juan Esteban"
    })

def about(request):
    return render(request, "about.html")