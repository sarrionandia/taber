from django.test import TestCase

from data.test import generate_objects
from draw.controller.InitialDrawController import InitialDrawController
from draw.models import TournamentStateException, Tournament


class InitialDrawControllerTestCase(TestCase):

    def testProducesCorrectNumberOfDebatesFor20Teams(self):
        for i in range(0, 20):
            team = generate_objects.valid_team()
            team.save()

        controller = InitialDrawController()
        result = controller.initial_draw()

        self.assertEqual(5, len(result), "Didn't produce the correct number of debates: " + str(len(result)))

    def testProducesCorrectNumberOfDebatesFor40Teams(self):
        for i in range(0, 40):
            team = generate_objects.valid_team()
            team.save()

        controller = InitialDrawController()
        result = controller.initial_draw()

        self.assertEqual(10, len(result), "Didn't produce the correct number of debates: " + str(len(result)))

    def testRaisesExceptionForBadNumberOfTeams(self):
        for i in range(0, 9):
            team = generate_objects.valid_team()
            team.save()

        controller = InitialDrawController()
        with self.assertRaises(TournamentStateException):
            controller.initial_draw()

    def testRaisesExceptionForZeroTeams(self):
        controller = InitialDrawController()
        with self.assertRaises(TournamentStateException):
            controller.initial_draw()


    def testRaisesExceptionIfNotRoundZero(self):
        tournament = Tournament.instance()
        tournament.round = 1
        tournament.save()

        for i in range(0, 20):
            team = generate_objects.valid_team()
            team.save()


        with self.assertRaises(TournamentStateException):
            controller = InitialDrawController()
            controller.initial_draw()

    def testChangesRoundNumber(self):
        round = Tournament.instance().round

        for i in range(0, 20):
            team = generate_objects.valid_team()
            team.save()

        controller = InitialDrawController()
        controller.initial_draw()

        self.assertEqual(round+1, Tournament.instance().round, "Didn't increment the round number")