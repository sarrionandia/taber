from django.db import models


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
    speaker1 = models.CharField(max_length=50)
    speaker2 = models.CharField(max_length=50)

    @property
    def total_team_points(self):
        from results.controllers.PointsController import PointsController
        controller = PointsController()
        from draw.models import Tournament
        return controller.total_points_for_team(self, Tournament.instance().round-1)

    @property
    def speakers(self):
        return [self.speaker1, self.speaker2]

    def __str__(self):
        return self.institution.__str__() + ' ' + self.name


class Judge(models.Model):
    name = models.CharField(max_length=80)
    institution = models.ForeignKey(Institution)

    def __str__(self):
        return self.name + ' <' + self.institution.__str__() + '>'


class Venue(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

