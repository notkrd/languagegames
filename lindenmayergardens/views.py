from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Lsystem, Lrule
from .lindenmayergardening import IterateUpdateLsysKeyList, ParseLrules, LrulesToStr
from .forms import LsystemForm

# Create your views here.

class LindenmayerListView(ListView):
    model = Lsystem
    the_lsystems = Lsystem.objects.all()

def ablossoming(request, lsystem_id, num_iterations=10):
    lsystem = get_object_or_404(Lsystem, pk=lsystem_id)
    lsystem_iterations = IterateUpdateLsysKeyList(lsystem_id, int(num_iterations))
    return render(request, 'lindenmayergardens/ablossoming.html', {'lsystem': lsystem, 'lsystem_iterations': lsystem_iterations})

def asowing(request):    
    if request.method == 'POST':
        form = LsystemForm(request.POST)
        if form.is_valid():
            new_text = form.cleaned_data['sys_init_text']
            unparsed_lrules = form.cleaned_data['sys_rules']
            new_lsys = Lsystem.objects.create(init_text=new_text)
            ParseLrules(unparsed_lrules, new_lsys)
            return HttpResponseRedirect(reverse('apruning', kwargs={'lsystem_id': new_lsys.id}))
        
    else:
        form = LsystemForm()
        
    return render(request, 'lindenmayergardens/asowing.html', {'form': form})

def apruning(request, lsystem_id, num_iterations=10):
    the_lsys = get_object_or_404(Lsystem, pk=lsystem_id)
    the_lsys_iterations = IterateUpdateLsysKeyList(lsystem_id, int(num_iterations))
    if request.method == 'POST':
        form = LsystemForm(request.POST)
        if form.is_valid():
            new_text = form.cleaned_data['sys_init_text']
            unparsed_lrules = form.cleaned_data['sys_rules']
            disp_iterations = form.cleaned_data['display_iterations']
            Lrule.objects.filter(lsys = lsystem_id).delete()
            the_lsys.init_text = new_text
            ParseLrules(unparsed_lrules, the_lsys)
            the_lsys.save()
            return HttpResponseRedirect(reverse('apruning-iterations', kwargs={'lsystem_id': lsystem_id, 'num_iterations': disp_iterations}))
        
    elif request.method == 'GET':
        lsys_init_text = the_lsys.init_text
        lsys_str = LrulesToStr(lsystem_id)
        lsys_form_data = {'sys_init_text': lsys_init_text,
                          'sys_rules': lsys_str,
                          "display_iterations": num_iterations}
        form = LsystemForm(lsys_form_data)
            
    return render(request, 'lindenmayergardens/apruning.html', {'form': form, 'lsystem_id': lsystem_id, 'lsystem': the_lsys, 'num_iterations': num_iterations, 'lsystem_iterations': the_lsys_iterations})