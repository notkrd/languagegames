from django.conf.urls import url

from . import views
from .views import RnnDetailView, RnnListView

urlpatterns = [
    # ex: /polls/
    url(r'^$', RnnListView.as_view(), name='rnnreading-list'),
    url(r'^(?P<rnn_id>[0-9]+)/read/$', RnnDetailView.as_view(), name='rnnreading-detail'),
]
