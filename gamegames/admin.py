from django.contrib import admin
from .models import Game, Move

class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'how_to_play', 'turn_order', 'is_game_over', 'game_state', 'archetype']
    search_fields = ['name','how_to_play']

admin.site.register(Game, GameAdmin)
admin.site.register(Move)
