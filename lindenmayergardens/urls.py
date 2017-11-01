from django.conf.urls import url

from . import views
from lindenmayergardens.views import LindenmayerListView

urlpatterns = [
    # ex: /polls/
    url(r'^$', LindenmayerListView.as_view(), name='lindenmayer-list'),
    # ex: /sow/
    url(r'^sow/$', views.asowing, name='asowing'),
    # ex: /ablossoming/1/
    url(r'^(?P<lsystem_id>[0-9]+)/$', views.ablossoming, name='ablossoming'),
    # ex: /ablossoming/1/10
    url(r'^(?P<lsystem_id>[0-9]+)/(?P<num_iterations>[0-9]+)/$', views.ablossoming, name='ablossoming-iterations'),
    # ex: /ablossoming/1/prune/
    url(r'^(?P<lsystem_id>[0-9]+)/prune/$', views.apruning, name='apruning'),
    # ex: /ablossoming/1/prune/11
    url(r'^(?P<lsystem_id>[0-9]+)/(?P<num_iterations>[0-9]+)/prune/$', views.apruning, name='apruning-iterations')
]
