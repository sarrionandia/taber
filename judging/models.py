from django.core.exceptions import ValidationError
from django.db import models

from data.models import Judge
from draw.models import Debate, TournamentStateException


class Panel(models.Model):
    debate = models.ForeignKey(Debate)
    judges = models.ManyToManyField(Judge)
    chair = models.ForeignKey(Judge, related_name='chairing')

    def clean(self):
        for panel in Panel.objects.all():
            if panel != self and panel.debate == self.debate:
                raise ValidationError("That debate already has a panel")

    def __str__(self):
        return "R" + str(self.debate.round) + " " + str(self.debate.venue)