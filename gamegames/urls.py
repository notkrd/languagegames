from django.conf.urls import url

from . import views
from gamegames.views import GamesListView, GameDetailView, PlayGameView

urlpatterns = [
    # ex: /
    url(r'^$', GamesListView.as_view(), name='gamegames-list'),
    url(r'^victory/', views.victory, name='victory'),
    url(r'^game/(?P<game_id>[0-9]+)/', GameDetailView.as_view(), name='view-gamegame'),
    url(r'^play/(?P<game_id>[0-9]+)/', PlayGameView.as_view(), name='play-gamegame'),
]