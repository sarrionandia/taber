from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator

class Institution(models.Model):
    name = models.CharField(max_length=50);

    @property
    def teams(self):
        return Team.objects.filter(institution=self)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution)

    @property
    def speakers(self):
        return Speaker.objects.filter(team=self).order_by('id')

    def __str__(self):
        return self.institution.__str__() + ' ' + self.name


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.name + ' <' + self.team.__str__() + '>'

    def clean(self):
        num_in_team = Speaker.objects.filter(team=self.team).count()
        if num_in_team >= 2:
            raise ValidationError('There can only be two speakers per team')

class Judge(models.Model):
    name = models.CharField(max_length=80)
    institution = models.ForeignKey(Institution)

    def __str__(self):
        return self.name + ' <' + self.institution.__str__() + '>'

class Venue(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

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
