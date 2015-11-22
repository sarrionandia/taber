from tab.models import Venue
from django.test import TestCase


class VenueTestCase(TestCase):

    def setUp(self):
        Venue.objects.create(name='Dungeon')

    def test_return_string(self):
        expected = 'Dungeon'
        actual = Venue.objects.get(name='Dungeon').__str__()
        self.assertEqual(expected, actual)