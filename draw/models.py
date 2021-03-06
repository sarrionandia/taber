from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

import results
from data.models import Team, Venue, Judge
from draw.controller.helpers.DebateHelpers import debate_as_strings
from draw.validators import DebateValidator


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

    @property
    def round_with_results(self):
        from results.controllers.ResultsController import ResultsController
        controller = ResultsController()
        if controller.results_entered_for_round(self.round):
            return self.round
        else:
            return self.round - 1

class Debate(models.Model):
    round = models.IntegerField(validators=[MinValueValidator(1)])
    OG = models.ForeignKey(Team, related_name='OG')
    OO = models.ForeignKey(Team, related_name='OO')
    CG = models.ForeignKey(Team, related_name='CG')
    CO = models.ForeignKey(Team, related_name='CO')
    venue = models.ForeignKey(Venue, null=True, blank=True)

    @property
    def result(self):
        if self.results.count() > 0:
            return self.results.first()
        else:
            return results.models.Result(debate=self)

    @property
    def has_result(self):
        return self.results.count() > 0

    def positions(self):
        return {
            'OG' : self.OG,
            'OO' : self.OO,
            'CG' : self.CG,
            'CO' : self.CO
                 }

    def __str__(self):
        return 'R' + str(self.round) + "<" + self.venue.name + ">"

    @property
    def as_strings_with_results(self):
        return debate_as_strings(self)

    def clean(self):
        DebateValidator.validate(self, Debate.objects.filter(round=self.round))

