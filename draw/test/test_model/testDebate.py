from django.core.exceptions import ValidationError
from django.test import TestCase

from data.test import generate_objects


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

    def test_positions(self):
        debate = generate_objects.valid_debate()
        positions = debate.positions()
        self.assertEqual(debate.OG, positions['OG'])
        self.assertEqual(debate.OO, positions['OO'])
        self.assertEqual(debate.CG, positions['CG'])
        self.assertEqual(debate.CO, positions['CO'])

    def test_gets_result_that_exists(self):
        result = generate_objects.valid_result_with_debate()
        debate = result.debate
        self.assertEqual(debate.result, result, "Didn't return the result for the debate")

    def test_gets_empty_result_withouht_existing_result(self):
        debate = generate_objects.valid_debate()
        self.assertIsNotNone(debate.result, "Didn't return an empty result when there is no existing result")