from django.core.exceptions import ValidationError
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

    def clean(self):
        self.check_positions_awarded()

    def check_positions_awarded(self):
        results = [self.og, self.oo, self.cg, self.co]
        if not 0 in results:
            raise ValidationError("4th was not awarded")
        if not 1 in results:
            raise ValidationError("3rd was not awarded")
        if not 2 in results:
            raise ValidationError("2nd was not awarded")
        if not 3 in results:
            raise ValidationError("1st was not awarded")