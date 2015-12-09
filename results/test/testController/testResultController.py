from django.test import TestCase

from data.test import generate_objects
from draw.controller.InitialDrawController import InitialDrawController
from draw.models import TournamentStateException, Tournament, Debate
from results.controllers import ResultsController
from results.models import Result


class ResultControllerTestCase(TestCase):
    def testRaisesExceptionForRoundNotDrawn(self):
        tournament = Tournament.instance()
        tournament.round = 1
        tournament.save()
        with self.assertRaises(TournamentStateException):
            ResultsController.results_entered_for_round(10)

    def testReturnsFalseForRoundWithoutAnyResults(self):
        self.setupIVR1()
        self.assertFalse(ResultsController.results_entered_for_round(1), "No results entered but returned true")

    def testReturnsTrueForRoundWithAllResults(self):
        self.setupIVR1()

        for debate in Debate.objects.filter(round=1):
            self.validResult(debate)

        self.assertTrue(ResultsController.results_entered_for_round(1), "All results entered but returned false")

    def validResult(self, debate):
        result = Result(debate=debate)
        result.ogsp1, result.ogsp2 = 90, 90
        result.oosp1, result.oosp2 = 80, 80
        result.cgsp1, result.cgsp2 = 70, 70
        result.cosp1, result.cosp2 = 60, 60

        result.og, result.oo, result.cg, result.co = 3, 2, 1, 0
        result.save()

        return result


    def setupIVR1(self):
        for i in range(0, 20):
            team = generate_objects.valid_team()
            team.save()

        for i in range(0, 5):
            venue = generate_objects.valid_venue()
            venue.save()

        controller = InitialDrawController()
        controller.initial_draw()
