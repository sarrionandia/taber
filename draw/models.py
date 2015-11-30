from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from data.models import Team, Venue, Judge

class Tournament(models.Model):
    round = models.IntegerField()

    def clean(self):
        if (Tournament.objects.count() > 0 and
                self.id != Tournament.objects.get().id):
            raise ValidationError("Only one tournament can be created")

class Debate(models.Model):
    round = models.IntegerField(validators=[MinValueValidator(1)])
    venue = models.ForeignKey(Venue)
    OG = models.ForeignKey(Team, related_name='OG')
    OO = models.ForeignKey(Team, related_name='OO')
    CG = models.ForeignKey(Team, related_name='CG')
    CO = models.ForeignKey(Team, related_name='CO')
    chair = models.ForeignKey(Judge)

    def positions(self):
        return {
            'OG' : self.OG,
            'OO' : self.OO,
            'CG' : self.CG,
            'CO' : self.CO
                 }

    def clean(self):
        self.validate_team_unique()
        self.validate_venue_unique()
        self.validate_chair_unique()

    def validate_venue_unique(self):
        if(Debate.objects.filter(round=self.round, venue=self.venue).count() >= 1):
            raise ValidationError("A venue can't be used for multiple debates in the same round")

    def validate_team_unique(self):
        if (len(self.positions().values()) > (len(set(self.positions().values())))):
            raise ValidationError("A team can't be in two positions in one room")

        debates = Debate.objects.all()

        for debate in debates:
            if (debate != self):
                if any(x in debate.positions().values() for x in self.positions().values()):
                    raise ValidationError("A team can't be in two debates in the same round")

    def validate_chair_unique(self):
        if(Debate.objects.filter(round=self.round, chair=self.chair).count() >= 1):
            raise ValidationError("A chair judge can't be used for multiple debates in the same round")
