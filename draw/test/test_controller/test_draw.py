from django.test import TestCase

from draw.controller.DrawController import DrawController
from draw.models import TournamentStateException
from mock import Mock


class DrawControllerTestCase(TestCase):

    def setUp(self):
        self.controller = DrawController()
        self.teams = [
            Mock(), Mock(), Mock(), Mock()
        ]

        points_controller = Mock()
        points_controller.total_points_for_team.return_value = 3
        self.controller.pointsController = points_controller

        self.results_controller = Mock()
        self.controller.resultsController = self.results_controller

    def testThrowsExceptionIfNotAllDebatesHaveResult(self):
        self.results_controller.results_entered_for_round.return_value = False
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

    def testAllPoolsContainAList(self):
        pools = self.controller.create_pools(self.teams, 4)
        for pool in pools.values():
            self.assertTrue(isinstance(pool, list), "Each pool should be a list, even if empty")

    def testNumberOfTeamsAreAddedToPools(self):
        pools = self.controller.create_pools(self.teams, 2)
        self.assertEqual(4, len(pools[3]))

    def testRemoveEmptyPools(self):
        pools = self.controller.create_pools(self.teams, 2)
        pools = self.controller.remove_empty(pools)
        self.assertEqual(1, len(pools.keys()))

    def testBalancePoolsReturnsExceptionForInvalidTeamNumber(self):
        pools = {
            1 : [Mock(), Mock(), Mock()],
            2: [Mock(), Mock()]
        }
        with self.assertRaises(ValueError):
            self.controller.balance_pools(pools)