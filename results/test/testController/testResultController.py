from django.test import TestCase

from data.test import generate_objects

from draw.models import TournamentStateException, Tournament, Debate
from results.controllers.ResultsController import ResultsController


class ResultControllerTestCase(TestCase):

    resultController = None

    def setUp(self):
        self.resultController = ResultsController()

    def testRaisesExceptionForRoundNotDrawn(self):
        tournament = Tournament.instance()
        tournament.round = 1
        tournament.save()
        with self.assertRaises(TournamentStateException):
            self.resultController.results_entered_for_round(10)

    def testReturnsFalseForRoundWithoutAnyResults(self):
        generate_objects.setup_IV_R1()
        self.assertFalse(self.resultController.results_entered_for_round(1), "No results entered but returned true")

    def testReturnsTrueForRoundWithAllResults(self):
        generate_objects.setup_IV_R1()

        for debate in Debate.objects.filter(round=1):
            generate_objects.valid_result_given_debate(debate)

        self.assertTrue(self.resultController.results_entered_for_round(1), "All results entered but returned false")

    def testReturnsFalseForPartiallyEnteredRound(self):
        generate_objects.setup_IV_R1()
        generate_objects.valid_result_given_debate(Debate.objects.first())

        self.assertFalse(self.resultController.results_entered_for_round(1), "Only some results entered but returned true")

    def testGetResultForRound(self):
        result = generate_objects.valid_result_with_debate()
        debate = result.debate

        error = "Result not retrieved correctly for round"

        self.assertEqual(result, self.resultController.result_for_team(debate.OG, 1), error)
        self.assertEqual(result, self.resultController.result_for_team(debate.OO, 1), error)
        self.assertEqual(result, self.resultController.result_for_team(debate.CG, 1), error)
        self.assertEqual(result, self.resultController.result_for_team(debate.CO, 1), error)

    def testCorrectTeamPointsForRound(self):
        result = generate_objects.valid_result_with_debate()

        self.assertEqual(result.og, self.resultController.team_points_for_team(result.debate.OG, 1))
        self.assertEqual(result.oo, self.resultController.team_points_for_team(result.debate.OO, 1))
        self.assertEqual(result.cg, self.resultController.team_points_for_team(result.debate.CG, 1))
        self.assertEqual(result.co, self.resultController.team_points_for_team(result.debate.CO, 1))
