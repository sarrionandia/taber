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
        generate_objects.setup_IV_R1()
        self.assertFalse(ResultsController.results_entered_for_round(1), "No results entered but returned true")

    def testReturnsTrueForRoundWithAllResults(self):
        generate_objects.setup_IV_R1()

        for debate in Debate.objects.filter(round=1):
            generate_objects.valid_result_given_debate(debate)

        self.assertTrue(ResultsController.results_entered_for_round(1), "All results entered but returned false")

    def testReturnsFalseForPartiallyEnteredRound(self):
        generate_objects.setup_IV_R1()
        generate_objects.valid_result_given_debate(Debate.objects.first())

        self.assertFalse(ResultsController.results_entered_for_round(1), "Only some results entered but returned true")

