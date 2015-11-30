from django.test import TestCase

from data.models import Team, Judge, Venue
from data.test import generate_objects
from draw.controller.InitialDrawController import InitialDrawController


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
