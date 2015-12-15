from django.test import TestCase

from data.test import generate_objects
from draw.controller.DrawController import DrawController
from draw.models import TournamentStateException


class DrawControllerTestCase(TestCase):

    def setUp(self):
        self.controller = DrawController()

    def testThrowsExceptionIfNotAllDebatesHaveResult(self):
        generate_objects.setup_IV_R1()
        with self.assertRaises(TournamentStateException):
            self.controller.create_pools([], 3)

    def testCreateBlankPoolsReturnsEmptyForRoundZero(self):
        pools = self.controller.create_blank_pools(0)
        self.assertEqual(0, len(pools.keys()), "Should not create any pools for round zero")

    def testCreateBlankPoolsReturnsCorrectNumberOfPoolsForR1(self):
        pools = self.controller.create_blank_pools(1)
        self.assertEqual(4, len(pools.keys()), "Should be four possible pools for Round 1")