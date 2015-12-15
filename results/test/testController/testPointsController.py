from django.test import TestCase

from results.controllers.PointsController import PointsController
from mock import Mock, call


class PointsControllerTestCase(TestCase):

    def setUp(self):
        self.og = Mock()
        self.oo = Mock()
        self.cg = Mock()
        self.co = Mock()
        self.points_controller = PointsController()
        self.results_controller = Mock()
        debate = Mock(OG=self.og, OO=self.oo, CG=self.cg, CO=self.co)
        result = Mock(debate=debate, og=0, oo=1, cg=2, co=3)
        self.results_controller.result_for_team.return_value = result
        self.points_controller.results_controller = self.results_controller

    def testGetTeamPoints(self):
        self.assertEqual(0, self.points_controller.team_points_for_team(self.og, 1), "Did not get correct team score for OG")
        self.assertEqual(1, self.points_controller.team_points_for_team(self.oo, 1), "Did not get correct team score for OO")
        self.assertEqual(2, self.points_controller.team_points_for_team(self.cg, 1), "Did not get correct team score for CG")
        self.assertEqual(3, self.points_controller.team_points_for_team(self.co, 1), "Did not get correct team score for CO")

    def testGetTeamPointsCallsResultController(self):
        self.points_controller.team_points_for_team(self.og, 1)
        self.results_controller.result_for_team.assert_called_once_with(self.og, 1)

    def testGetTotalPointsCallsCorrectNumberOfRounds(self):
        self.points_controller.total_points_for_team(self.og, 3)
        calls = [call(self.og, 1), call(self.og, 2), call(self.og, 3)]
        self.results_controller.result_for_team.assert_has_calls(calls, any_order=True)