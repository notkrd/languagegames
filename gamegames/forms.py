from django import forms

class MoveChoiceForm(forms.Form):
    player_move = forms.ChoiceField(label="Your move")