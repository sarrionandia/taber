from django.core.exceptions import ValidationError
from django.forms import ModelForm

from data.models import Judge
from draw.models import Debate
from judging.models import Panel


class PanelForm(ModelForm):
    class Meta:
        model = Panel
        fields = "__all__"

    def clean(self):
        judges = self.cleaned_data.get('judges')
        chair = self.cleaned_data.get('chair')
        if chair not in judges:
            raise ValidationError("Chair is not in the judging list")

        return self.cleaned_data
