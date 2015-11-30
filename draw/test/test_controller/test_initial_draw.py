from django.test import TestCase

from data.models import Team, Judge, Venue
from data.test import generate_objects
from draw.controller.InitialDrawController import InitialDrawController


class InitialDrawControllerTestCase(TestCase):

    def testProducesCorrectNumberOfDebates(self):

        for i in range(0, 19):
            team = generate_objects.valid_team()
            team.save()

        for i in range(0, 4):
            venue = generate_objects.valid_venue()
            venue.save()

        for i in range(0, 4):
            judge = generate_objects.valid_judge()
            judge.save()

        controller = InitialDrawController()
        result = controller.initialDraw()

        self.assertEqual(5, result.count(), "Didn't produce the correct number of debates")