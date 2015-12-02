from django.test import TestCase

from data.test import generate_objects
from draw.controller.VenueMapper import VenueMapper
from draw.models import TournamentStateException


class VenueMapperTestCase(TestCase):
    def testRaisesExceptionForNotEnoughVenues(self):
        generate_objects.valid_venue()
        for i in range(0, 20):
            debate = generate_objects.valid_debate()
            debate.save()
        controller = VenueMapper()
        with self.assertRaises(TournamentStateException):
            controller.map_venues(1)

