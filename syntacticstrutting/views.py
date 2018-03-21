from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def placeholder_view(request):
    return HttpResponse('You already know all the well-formed formulas if you\'re from this tongue. Elaboration pending. <p class="nope"><a href="/">HOME</a></p>')