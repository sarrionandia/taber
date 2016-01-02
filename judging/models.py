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

        for judge in self.judges.all():
            for panel in judge.panel_set.all():
                if panel != self and panel.debate.round == self.debate.round:
                    raise TournamentStateException("Judge " + str(judge) + " is already on a panel for this round")