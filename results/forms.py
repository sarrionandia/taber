from django.forms import ModelForm
from results.models import Result

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['ogsp1',
                  'ogsp2',
                  'oosp1',
                  'oosp2',
                  'cgsp1',
                  'cgsp2',
                  'cosp1',
                  'cosp2'
                  ]
