import requests
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def index(request):

    url = "https://imdb8.p.rapidapi.com/title/find"

    querystring = 'q={}'

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "c994e4f6d4mshed2cac0ce4cf113p1dd3c5jsn68075801cc26"
    }

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            new_movie = form['title']
            existing_movie_count = Movie.objects.filter(title=new_movie).count()

            if existing_movie_count == 0:
                response = requests.get(url, headers=headers, params=querystring.format(new_movie)).json()
                form.save()

    form = MovieForm()
    movies = Movie.objects.all()
    movie_data = []

    for movie in movies:
        response = requests.get(url, headers=headers, params=querystring.format(movie)).json()

        movie_info = {
            'search_title': movie.title,
            'title': response['results'][0]['title'],
            'year': response['results'][0]['year'],
            'img': response['results'][0]['image']['url']
        }

        movie_data.append(movie_info)

    context = {'movie_data': movie_data, 'form': form}
    return render(request, 'movie/movie.html', context)

def delete_movie(request, search_title):
    Movie.objects.get(title=search_title).delete()
    return redirect('home')