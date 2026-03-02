from django.shortcuts import render
from .models import Movie

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})
    
def statistics_view(request):

    all_movies = Movie.objects.all()

    # =========================
    # 📊 MOVIES POR AÑO
    # =========================
    movie_counts_by_year = {}

    for movie in all_movies:
        year = movie.year if movie.year else "None"

        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1

    plt.figure(figsize=(8, 6))
    bar_positions = range(len(movie_counts_by_year))
    plt.bar(bar_positions, movie_counts_by_year.values())
    plt.title('Movies per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_png = buffer.getvalue()
    buffer.close()

    graphic_year = base64.b64encode(image_png).decode('utf-8')

    # =========================
    # 🎬 MOVIES POR GÉNERO
    # =========================
    movie_counts_by_genre = {}

    for movie in all_movies:
        genre = movie.genre if movie.genre else "None"

        if genre in movie_counts_by_genre:
            movie_counts_by_genre[genre] += 1
        else:
            movie_counts_by_genre[genre] = 1

    plt.figure(figsize=(8, 6))
    bar_positions = range(len(movie_counts_by_genre))
    plt.bar(bar_positions, movie_counts_by_genre.values())
    plt.title('Movies per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions, movie_counts_by_genre.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_png = buffer.getvalue()
    buffer.close()

    graphic_genre = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'statistics.html', {
        'graphic_year': graphic_year,
        'graphic_genre': graphic_genre
    })