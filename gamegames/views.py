from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView
from .models import Game, _GAME_CONTINUES, _GAME_DRAWN, _GAME_LOST, _GAME_WON
from .forms import MoveChoiceForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.http.response import HttpResponseRedirect, HttpResponse
from .models import *

# Create your views here.

class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'how_to_play', 'turn_order', 'is_game_over', 'game_state', 'archetype', 'fields_to_display', 'victory_conditions', 'loss_conditions', 'draw_conditions']

class GamesListView(ListView):
    model = Game
    queryset = Game.objects.filter(archetype=True)

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
    pk_url_kwarg = "game_id"
    
class PlayGameView(UpdateView):
    model = Game
    context_object_name = 'game'
    pk_url_kwarg = 'game_id'
    template_name = 'gamegames/play_game.html'
    form_class = MoveChoiceForm
    
    
    def get_form_kwargs(self):
        kwargs = super(PlayGameView, self).get_form_kwargs()

        # get users, note: you can access request using: self.request

        kwargs['the_game'] = self.object
        return kwargs
    
    def get_initial(self):
        possible_moves = filter(lambda m: m.for_players[0], self.object.move_set.all())
        move_choices = list(map(lambda m: (m.name, m), possible_moves))
        initial_vals = {'Your move': move_choices}
        return initial_vals
    
    def form_valid(self, form):
        the_game = self.object
        the_id = the_game.id
        the_move = form.cleaned_data['Your move']
        if self.object.archetype:
            old_moves = list(the_game.move_set.all())
            the_game.id = None
            the_game.archetype = False
            the_game.save()
            the_id = the_game.id
            for a_move in old_moves:
                if a_move != the_move:
                    a_move.id = None
                    a_move.game = the_game
                    a_move.save()
            the_move.id = None
            the_move.game = the_game
            the_move.save()
        the_move.make_move()
        return HttpResponseRedirect(reverse('play-gamegame', kwargs={'game_id': the_id}))

def victory(request, game_id=0):
    return render(request, 'gamegames/victory.html')

def defeat(request, game_id=0):
    return render(request, 'gamegames/defeat.html')

def checkgame(request, game_id):
    the_game = get_object_or_404(Game, pk=game_id)
    game_state = the_game.check_game_state()
    if game_state == _GAME_WON:
        return HttpResponseRedirect(reverse('victory-gamegame'))
    elif game_state == _GAME_LOST:
        return HttpResponseRedirect(reverse('defeat-gamegame'))
    elif game_state == _GAME_DRAWN:
        return HttpResponse('You drew. You can\'t go back on a compromise')
    else:
        return HttpResponseRedirect(reverse('play-gamegame', kwargs={'game_id': game_id}))