from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.placeholder_view, name='placeholder'),
]