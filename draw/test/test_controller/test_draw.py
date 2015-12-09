from django.test import TestCase

from data.test import generate_objects
from draw.controller.DrawController import DrawController
from draw.models import TournamentStateException, Tournament


class Teams(object):
    pass


class DrawControllerTestCase(TestCase):
    def testCreatePoolsWithEmptyList(self):
        teams = []
        controller = DrawController()
        self.assertEqual(0, len(controller.create_pools()))

    def testCreatePoolsWithNone(self):
        teams = None
        controller = DrawController()
        self.assertEqual(0, len(controller.create_pools()))

    def testThrowsExceptionIfNotAllDebatesHaveResult(self):
        generate_objects.setup_IV_R1()
        with self.assertRaises(TournamentStateException):
            controller = DrawController()
            controller.create_pools()