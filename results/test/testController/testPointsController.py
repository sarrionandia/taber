from django.test import TestCase

from results.controllers.PointsController import PointsController
from mock import Mock


class PointsControllerTestCase(TestCase):

    def testGetTeamPoints(self):

        og = Mock()
        oo = Mock()
        cg = Mock()
        co = Mock()

        points_controller = PointsController()
        results_controller = Mock()

        debate = Mock(OG=og, OO=oo, CG=cg, CO=co)
        result = Mock(debate=debate, og=0, oo=1, cg=2, co=3)


        results_controller.result_for_team.return_value = result
        points_controller.results_controller = results_controller

        self.assertEqual(0, points_controller.team_points_for_team(og, 1), "Did not get correct team score for OG")
        self.assertEqual(1, points_controller.team_points_for_team(oo, 1), "Did not get correct team score for OO")
        self.assertEqual(2, points_controller.team_points_for_team(cg, 1), "Did not get correct team score for CG")
        self.assertEqual(3, points_controller.team_points_for_team(co, 1), "Did not get correct team score for CO")
