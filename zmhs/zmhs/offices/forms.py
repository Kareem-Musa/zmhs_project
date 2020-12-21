from django import forms
from zmhs.offices.models import HQuarter , Sector
from zmhs.locations.models import State

class HqForm(forms.ModelForm):

    class Meta :
        model = HQuarter
        fields = ('name','state')

    def __init__(self,*args , **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['state'].widget.attrs.update({'class':'form-control','placeholder':'الولاية'})
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'الامانة'})

class SectorForm(forms.ModelForm):
    class Meta :
        model = Sector
        fields = ('name','hquarter')

    def __init__(self,*args , **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'القطاع'})
        self.fields['hquarter'].widget.attrs.update({'class':'form-control','placeholder':'الامانة'})
