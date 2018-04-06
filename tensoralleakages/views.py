from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import RnnReading

# Create your views here.

class RnnDetailView(DetailView):
    model = RnnReading
    context_object_name = 'rnn'
    pk_url_kwarg = 'rnn_id'
    
class RnnListView(ListView):
    model = RnnReading
    queryset = RnnReading.objects.all()