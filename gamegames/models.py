from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

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
    
    def check_game_state(self):
        for a_cond in self.victory_conditions:
            if a_cond <= self.game_state:
                return _GAME_WON
        for a_cond in self.loss_conditions:
            if a_cond <= self.game_state:
                return _GAME_LOST
        for a_cond in self.draw_conditions:
            if a_cond <= self.game_state:
                return _GAME_DRAWN
        return _GAME_CONTINUES
            
class Move(models.Model):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    
    requires = JSONField(default=list())
    sets = JSONField(default=list())
    removes = JSONField(default=list())
    adds = JSONField(default=list())
    
    for_players = ArrayField(base_field=models.BooleanField(), default=[True, True], size=None)
    
    def is_valid(self):
        return self.requires <= self.game.game_state
    
    def consider_move(self):
        for a_change in self.sets:
            self.game.game_state[a_change[0]] = a_change[1]
            
        for a_change in self.removes:
            del self.game.game_state[a_change]
            
        for a_change in self.adds:
            self.game.game_state[a_change[0]] += a_change[1]
            
        return self.game.game_state
