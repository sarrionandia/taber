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

