from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from draw.models import Debate


class Result(models.Model):
    debate = models.ForeignKey(Debate, related_name='results')

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

    def total_speaks(self):
        return {
            'og' : self.ogsp1 + self.ogsp2,
            'oo' : self.oosp1 + self.oosp2,
            'cg' : self.cgsp1 + self.cgsp2,
            'co' : self.cosp1 + self.cosp2
        }

    def positions(self):
        return {
            'og' : self.og,
            'oo' : self.oo,
            'cg' : self.cg,
            'co' : self.co
        }

    def clean(self):
        self.check_positions_awarded()
        self.check_position_matches_speaks()

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

    def check_position_matches_speaks(self):
        speaks = self.total_speaks()
        speaks_order = sorted(speaks, key=speaks.get)
        if self.positions()[speaks_order[0]] != 0:
            raise ValidationError("Team in 4th must have lowest speaker score")
        if self.positions()[speaks_order[1]] != 1:
            raise ValidationError("Team in 3rd must have second lowest speaker score")
        if self.positions()[speaks_order[2]] != 2:
            raise ValidationError("Team in 2nd must have second highest speaker score")
        if self.positions()[speaks_order[3]] != 3:
            raise ValidationError("Team in 1st must have highest speaker score")