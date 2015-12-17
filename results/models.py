import operator
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

    def __str__(self):
        return "Result for " + str(self.debate)

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
        from results.validators import ResultValidator
        ResultValidator.validate(self)


    def add_positions_from_speaks(self):
        speaks = self.total_speaks()
        positions = sorted(speaks, key=speaks.__getitem__)
        self.og = positions.index("og")
        self.oo = positions.index("oo")
        self.cg = positions.index("cg")
        self.co = positions.index("co")
