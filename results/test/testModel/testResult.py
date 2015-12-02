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
