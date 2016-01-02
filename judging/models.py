from django.db import models

from data.models import Judge
from draw.models import Debate, TournamentStateException


class Panel(models.Model):
    debate = models.ForeignKey(Debate)
    judges = models.ManyToManyField(Judge)
    chair = models.ForeignKey(Judge, related_name='chairing')

    def clean(self):
        if self.chair not in self.judges.all():
            raise TournamentStateException("Chair is not on the judging panel")