from django import forms
from zmhs.locations.models import State

class StateForm(forms.ModelForm):
    class Meta :
        model = State
        fields = ['name']
