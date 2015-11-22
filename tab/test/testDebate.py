from django.core.exceptions import ValidationError

from tab.models import Team, Venue, Judge, Debate, Institution
import generate_objects
from django.test import TestCase


class DebateTestCase(TestCase):

    def test_valid_creation(self):
        debate = generate_objects.valid_debate()
        debate.full_clean()

    def test_no_round_number(self):
        debate = generate_objects.valid_debate()
        debate.round = None

        with self.assertRaises(ValidationError):
            debate.full_clean()

    def test_duplicate_team_in_room(self):
        debate = generate_objects.valid_debate()
        debate.OG = debate.CO

        with self.assertRaises(ValidationError):
            debate.full_clean()

    def test_duplicate_team_in_round(self):
        debate1 = generate_objects.valid_debate()
        debate1.save()

        debate2 = generate_objects.valid_debate()
        debate2.CO = debate1.OG
        with self.assertRaises(ValidationError):
            debate2.full_clean()

    def test_round_invalid(self):
        debate = generate_objects.valid_debate()
        debate.round = 0
        with self.assertRaises(ValidationError):
            debate.full_clean()

    def test_duplicate_venue(self):
        debate1 = generate_objects.valid_debate()
        debate1.save()

        debate2 = generate_objects.valid_debate()
        debate2.venue = debate1.venue

        with self.assertRaises(ValidationError):
            debate2.full_clean()

    def test_same_venue_in_multiple_rounds(self):
        debate1 = generate_objects.valid_debate()
        debate1.save()

        debate2 = generate_objects.valid_debate()
        debate2.round = debate1.round + 1
        debate2.venue = debate1.venue

        debate2.clean()

    def test_duplicate_chair(self):
        debate1 = generate_objects.valid_debate()
        debate2 = generate_objects.valid_debate()
        debate2.chair = debate1.chair

        debate1.save()
        with self.assertRaises(ValidationError):
            debate2.full_clean()

    def test_positions(self):
        debate = generate_objects.valid_debate()
        positions = debate.getPositions()
        self.assertEqual(debate.OG, positions['OG'])
        self.assertEqual(debate.OO, positions['OO'])
        self.assertEqual(debate.CG, positions['CG'])
        self.assertEqual(debate.CO, positions['CO'])


