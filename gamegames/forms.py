from django import forms
from .models import Game, Move

class MoveChoiceForm(forms.ModelForm):
    
    def __init__(self, the_game, *args, **kwargs):
        super(MoveChoiceForm, self).__init__(*args, **kwargs)
        self.fields['Your move'] = forms.ModelChoiceField(
            queryset=Move.objects.filter(game = the_game)
        )
        
    class Meta:
        model = Move
        fields = []