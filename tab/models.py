from django.db import models

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

class Judge(models.Model):
    name = models.CharField(max_length=80)
    institution = models.ForeignKey(Institution)

    def __str__(self):
        return self.name + ' <' + self.institution.__str__() + '>'