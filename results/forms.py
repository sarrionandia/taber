from django import forms
from django.forms import ModelForm
from results.models import Result

class ResultForm(ModelForm):

    class Meta:
        model = Result
        fields = ['debate',
                  'ogsp1',
                  'ogsp2',
                  'oosp1',
                  'oosp2',
                  'cgsp1',
                  'cgsp2',
                  'cosp1',
                  'cosp2'
                  ]

        speak_attrs = {
            'type' : 'number',
            'class' : 'form-control',
            'min' : 0,
            'max' : 100
    }

        widgets = {
            "ogsp2":forms.TextInput(attrs=speak_attrs.copy()),
            "ogsp1":forms.TextInput(attrs=speak_attrs.copy()),
            "oosp1":forms.TextInput(attrs=speak_attrs.copy()),
            "oosp2":forms.TextInput(attrs=speak_attrs.copy()),
            "cgsp1":forms.TextInput(attrs=speak_attrs.copy()),
            "cgsp2":forms.TextInput(attrs=speak_attrs.copy()),
            "cosp1":forms.TextInput(attrs=speak_attrs.copy()),
            "cosp2":forms.TextInput(attrs=speak_attrs.copy()),
        }
