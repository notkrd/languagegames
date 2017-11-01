from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import Game
from django.views.generic.detail import DetailView

# Create your views here.

class GamesListView(ListView):
    model = Game
    queryset = Game.objects.filter(archetype=True)

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
    pk_url_kwarg = "game_id"
    
class PlayGameView(DetailView):
    model = Game
    context_object_name = 'game'
    pk_url_kwarg = 'game_id'
    template_name = 'gamegames/play_game.html'

def victory(request):
    return HttpResponse("You win.")