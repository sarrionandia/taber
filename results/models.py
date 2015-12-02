from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from draw.models import Debate


class Result(models.Model):
    debate = models.ForeignKey(Debate)

    ogsp1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    ogsp2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    oosp1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    oosp2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    cgsp1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    cgsp2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    cosp1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    cosp2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    og = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    oo = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    cg = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    co = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
