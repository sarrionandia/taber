from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=50);

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution)

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
    Chair = models.ForeignKey(Judge)

    def getPositions(self):
        return {
            'OG' : self.OG,
            'OO' : self.OO,
            'CG' : self.CG,
            'CO' : self.CO
                 }

    def clean(self):
        if (len(self.getPositions().values()) > (len(set(self.getPositions().values())))):
            raise ValidationError("A team can't be in two positions in one room")
