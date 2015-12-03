from django.test import TestCase

from data.test import generate_objects
from draw.controller.DrawController import DrawController
from draw.models import TournamentStateException, Tournament


class DrawControllerTestCase(TestCase):
    def testCreatePoolsWithEmptyList(self):
        teams = []
        controller = DrawController()
        self.assertEqual(0, len(controller.create_pools(teams)))