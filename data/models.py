from django.db import models

import draw


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
    def speakers(self):
        return [self.speaker1, self.speaker2]

    def __str__(self):
        return self.institution.__str__() + ' ' + self.name

    def debate_for_round(self, round):
        debates = draw.models.Debate.objects.filter(round=round)
        if debates.filter(OG=self).count() > 0:
            return debates.filter(OG=self).first()
        if debates.filter(OO=self).count() > 0:
            return debates.filter(OO=self).first()
        if debates.filter(CG=self).count() > 0:
            return debates.filter(CG=self).first()
        if debates.filter(CO=self).count() > 0:
            return debates.filter(CO=self).first()
        return None


class Judge(models.Model):
    name = models.CharField(max_length=80)
    institution = models.ForeignKey(Institution)

    def __str__(self):
        return self.name + ' <' + self.institution.__str__() + '>'

class Venue(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

