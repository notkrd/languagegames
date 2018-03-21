from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.urls import reverse
import random

_GAME_CONTINUES, _GAME_WON, _GAME_LOST, _GAME_DRAWN = range(0,4)
_GAME_OVER_CHOICES = {
    (_GAME_CONTINUES, "GAME CONTINUES"),
    (_GAME_WON, "VICTORY"),
    (_GAME_LOST, "DEFEAT"),
    (_GAME_DRAWN, "DRAW"),}

_SEQUENTIAL, _SIMULTANEOUS = range(0,2)
_TURN_ORDER_CHOIECS = {
    (_SEQUENTIAL, "SEQUENTIAL"),
    (_SIMULTANEOUS, "SIMULTANEOUS")}

class Game(models.Model):
    name = models.CharField(max_length=200)
    how_to_play = models.TextField()
    turn_order = models.IntegerField(choices=_TURN_ORDER_CHOIECS)
    is_game_over = models.IntegerField(choices=_GAME_OVER_CHOICES)
    game_state = JSONField(blank=True)
    archetype = models.BooleanField()
    fields_to_display = ArrayField(base_field=models.CharField(max_length=200))
    
    
    victory_conditions = JSONField(blank=True)
    loss_conditions = JSONField(blank=True)
    draw_conditions = JSONField(blank=True)
    
    game_ai = models.TextField(blank=True, default="")
    
    def __str__(self):
        return self.name
    
    def dict_contains(self, dict1, dict2):
        for a_key in dict2.keys():
            if a_key not in dict1:
                return False
            elif dict1[a_key] != dict2[a_key]:
                return False
        return True
    
    def check_game_state(self):
        for a_cond in self.victory_conditions:
            if self.dict_contains(self.game_state, a_cond):
                return _GAME_WON
        for a_cond in self.loss_conditions:
            if self.dict_contains(self.game_state, a_cond):
                return _GAME_LOST
        for a_cond in self.draw_conditions:
            if self.dict_contains(self.game_state, a_cond):
                return _GAME_DRAWN
        return _GAME_CONTINUES
    
    def get_absolute_url(self):
        return reverse('play-gamegame', kwargs={'game_id': self.id})
            
class Move(models.Model):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    
    requires = JSONField(default=dict(),blank=True)
    sets = JSONField(default=dict(),blank=True)
    removes = JSONField(default=dict(),blank=True)
    adds = JSONField(default=dict(),blank=True)
    
    for_players = ArrayField(base_field=models.BooleanField(), default=[True, True], size=None)
    
    def __str__(self):
        return self.name
        
    def is_valid(self):
        return self.requires.items() <= self.game.game_state.items()
    
    def consider_move(self):
        for a_change in self.sets:
            self.game.game_state[a_change] = self.sets[a_change]
            
        for a_change in self.removes:
            del self.game.game_state[a_change]
            
        for a_change in self.adds:
            self.game.game_state[a_change] += self.sets[a_change]
            
        return self.game.game_state

    def make_move(self):
        if self.is_valid():
            new_state = self.consider_move()
            self.game.game_state = new_state
            exec(self.game.game_ai)
            self.game.save()