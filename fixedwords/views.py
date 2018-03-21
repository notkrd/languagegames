from django.shortcuts import render
from django.views.generic import ListView, DetailView
from fixedwords.models import JustText
from django.views.generic.edit import CreateView

# Create your views here.

class TextsList(ListView):
    model = JustText
    the_txts = JustText.objects.all()

class TextView(DetailView):
    model = JustText
    context_object_name = 'a_text'
    pk_url_kwarg = "txt_id"
    
class MakeText(CreateView):
    model = JustText
    fields = ['title','author','txt']