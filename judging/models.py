from django.db import models

from data.models import Judge
from draw.models import Debate


class Panel(models.Model):
    debate = models.ForeignKey(Debate)
    judges = models.ManyToManyField(Judge)