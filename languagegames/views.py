from django.shortcuts import render

def index_view(request):
    return render(request, 'global_templates/index.html')