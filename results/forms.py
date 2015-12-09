from django import forms
from results.models import Result

def get_widget():
    speak_attrs = {
        'type' : 'number',
        'class' : 'form-control',
        'min' : 0,
        'max' : 100,
        'placeholder' : '1-100',
        'required' : 'required',
    }
    return forms.TextInput(attrs=speak_attrs.copy())

class ResultForm(forms.Form):

    ogsp1 = forms.IntegerField(widget=get_widget())
    ogsp2 = forms.IntegerField(widget=get_widget())
    oosp1 = forms.IntegerField(widget=get_widget())
    oosp2 = forms.IntegerField(widget=get_widget())
    cgsp1 = forms.IntegerField(widget=get_widget())
    cgsp2 = forms.IntegerField(widget=get_widget())
    cosp1 = forms.IntegerField(widget=get_widget())
    cosp2 = forms.IntegerField(widget=get_widget())