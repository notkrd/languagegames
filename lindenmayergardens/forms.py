from django import forms

class LsystemForm(forms.Form):
    sys_init_text = forms.CharField(label="Seed text", widget=forms.TextInput(attrs={'size': '50'}))
    sys_rules = forms.CharField(label="L-system rules", widget=forms.Textarea(attrs={'cols': '75'}))
    
class NumIterationsForm(forms.Form):
    display_iterations = forms.IntegerField(label="# of iterations to display")