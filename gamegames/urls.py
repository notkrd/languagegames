from django.conf.urls import url

from . import views
from gamegames.views import GamesListView, GameDetailView, PlayGameView

urlpatterns = [
    # ex: /
    url(r'^$', GamesListView.as_view(), name='gamegames-list'),
    url(r'^victory/', views.victory, name='victory'),
    url(r'^victory/', views.victory, name='victory-gamegame'),
    url(r'^game/(?P<game_id>[0-9]+)/', GameDetailView.as_view(), name='view-gamegame'),
    url(r'^play/(?P<game_id>[0-9]+)/', PlayGameView.as_view(), name='play-gamegame'),
    url(r'^victory/(?P<game_id>[0-9]+)/', views.victory, name='victory-gamegame'),
    url(r'^defeat/', views.defeat, name='defeat-gamegame'),
    url(r'^check/(?P<game_id>[0-9]+)/', views.checkgame, name='checkgame'),
    url(r'^create/', views.GameCreateView.as_view(), name='make-gamegame'),
]