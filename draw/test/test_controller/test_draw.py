from django.test import TestCase

from data.test import generate_objects
from draw.controller.DrawController import DrawController
from draw.models import TournamentStateException
from mock import Mock


class DrawControllerTestCase(TestCase):

    def setUp(self):
        self.controller = DrawController()
        self.teams = [
            Mock(), Mock(), Mock(), Mock()
        ]

    def testThrowsExceptionIfNotAllDebatesHaveResult(self):
        generate_objects.setup_IV_R1()
        with self.assertRaises(TournamentStateException):
            self.controller.create_pools(self.teams, 3)

    def testCreateBlankPoolsReturnsEmptyForRoundZero(self):
        pools = self.controller.create_blank_pools(0)
        self.assertEqual(0, len(pools.keys()), "Should not create any pools for round zero")

    def testCreateBlankPoolsReturnsCorrectNumberOfPoolsForR1(self):
        pools = self.controller.create_blank_pools(1)
        self.assertEqual(4, len(pools.keys()), "Should be four possible pools for Round 1")

    def testCreatesRightNumberOfPools(self):
        pools = self.controller.create_pools(self.teams, 4)
        self.assertEqual(13, len(pools.keys()), "Should be 13 possible pools for Round 4")