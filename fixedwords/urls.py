from django.conf.urls import url

from .views import TextsList, TextView, MakeText
from .models import JustText

urlpatterns = [
    # ex: /
    url(r'^$', TextsList.as_view(), name='texts-list'),
    url(r'^txt/(?P<txt_id>[0-9]+)/', TextView.as_view(), name='read-text'),
    url(r'^txt/new/', MakeText.as_view(), name='new-text'),
]