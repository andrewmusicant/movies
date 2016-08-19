from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from .models import Movie, Rater, Rating
from django.http import Http404, HttpResponseRedirect
from django.db.models import Avg

from django.contrib.auth.forms import UserCreationForm
from .forms import RaterForm


# Create your views here.
def index(request):
    top_twenty = Movie.get_average_scores()
    context = {
        'Movies': top_twenty,
        }
    return render(request, 'movies/index.html', context)


def movie_view(request):
    all_movies = Movie.objects.all()
    context = {
        'all_movies': all_movies,
    }
    return render(request, 'movies/movie_view.html', context)


def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        average_score = movie.get_average_score()
    except Movie.DoesNotExist:
        raise Http404("Movie doesn't exist")
    context = {
        'movie': movie,
        'average_score': '{0:.2f}'.format(average_score),
    }
    return render(request, 'movies/movie_detail.html', context)


def user_view(request):
    all_raters = Rater.objects.all()
    context = {
        'all_raters': all_raters,
    }
    return render(request, 'movies/user_view.html', context)


def user_detail(request, rater_id):
    try:
        rater = Rater.objects.get(pk=rater_id)
    except Rater.DoesNotExist:
        raise Http404("Rater doesn't exist")
    context = {
        'rater': rater,
    }
    return render(request, 'movies/user_detail.html', context)


def register_user(request):
    if request.method == 'POST':
        rf = RaterForm(request.POST, prefix='rater')
        uf = UserCreationForm(request.POST, prefix='user')
        if rf.is_valid() * uf.is_valid():
            user = uf.save(commit=False)
            user.save()
            rater = rf.save(commit=False)
            rater.user_id = user.id
            rater.id = user.id
            rater.save()
            return HttpResponseRedirect('/')
    else:
        rf = RaterForm(prefix='rater')
        uf = UserCreationForm(prefix='user')
        context = {'raterform': rf, 'userform': uf}
        return render(request, 'registration/register.html', context)


def test_table(request):
    # Inspiration: https://datatables.net/examples/styling/bootstrap.html
    all_movies = Movie.objects.all()
    context = {
        'all_movies': all_movies,
    }
    return render(request, 'movies/test_table.html', context)
