from django.core.exceptions import ValidationError
from django.test import TestCase

from data.test import generate_objects
from results.models import Result


class ResultTestCase(TestCase):

    def testMinSpeakerScore(self):
        result = generate_objects.valid_result_with_debate()
        result.ogsp2 = -2
        with self.assertRaises(ValidationError):
            result.full_clean()

    def testMaxSpeakerScore(self):
        result = generate_objects.valid_result_with_debate()
        result.ogsp1 = 101
        with self.assertRaises(ValidationError):
            result.full_clean()

    def testMinTeamScore(self):
        result = generate_objects.valid_result_with_debate()
        result.og = -1
        with self.assertRaises(ValidationError):
            result.full_clean()

    def testMaxTeamScore(self):
        result = generate_objects.valid_result_with_debate()
        result.og = 4
        with self.assertRaises(ValidationError):
            result.full_clean()

    def testAllPositionsMustBeAwarded(self):
        result = generate_objects.valid_result_with_debate()
        result.og = 3
        result.co = 3
        with self.assertRaises(ValidationError):
            result.full_clean()

        result = generate_objects.valid_result_with_debate()
        result.og = 2
        result.oo = 2
        with self.assertRaises(ValidationError):
            result.full_clean()

    def testSpeakerScoreMustBeConsistentWithTeamScore(self):
        result = generate_objects.valid_result_with_debate()
        result.ogsp1=1
        result.ogsp2=1
        result.og = 3
        result.oo = 2
        result.cg = 1
        result.co = 0

        with self.assertRaises(ValidationError):
            result.full_clean()