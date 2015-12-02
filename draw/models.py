from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from data.models import Team, Venue, Judge

class TournamentStateException(Exception):
    pass

class Tournament(models.Model):
    round = models.IntegerField()

    def clean(self):
        if (Tournament.objects.count() > 0 and
                self.id != Tournament.objects.get().id):
            raise ValidationError("Only one tournament can be created")

    @staticmethod
    def instance():
        if Tournament.objects.all().count() > 0:
            return Tournament.objects.first()
        else:
            return Tournament(round=0)

class Debate(models.Model):
    round = models.IntegerField(validators=[MinValueValidator(1)])
    OG = models.ForeignKey(Team, related_name='OG')
    OO = models.ForeignKey(Team, related_name='OO')
    CG = models.ForeignKey(Team, related_name='CG')
    CO = models.ForeignKey(Team, related_name='CO')
    venue = models.ForeignKey(Venue, null=True, blank=True)

    def positions(self):
        return {
            'OG' : self.OG,
            'OO' : self.OO,
            'CG' : self.CG,
            'CO' : self.CO
                 }

    def clean(self):
        self.validate_team_unique()

    def validate_team_unique(self):
        if (len(self.positions().values()) > (len(set(self.positions().values())))):
            raise ValidationError("A team can't be in two positions in one room")

        debates = Debate.objects.all().filter(round=self.round)
        for debate in debates:
            if any(x in debate.positions().values() for x in self.positions().values()):
                raise ValidationError("A team can't be in two debates in the same round")
