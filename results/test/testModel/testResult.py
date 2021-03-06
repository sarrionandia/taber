from django.core.exceptions import ValidationError
from django.test import TestCase

from data.test import generate_objects
from draw.models import Tournament, TournamentStateException


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

    def testTotalSpeakerScore(self):
        result = generate_objects.valid_result_with_debate()
        total_speaks = result.total_speaks()

        self.assertEqual(total_speaks['og'], result.ogsp1 + result.ogsp2)
        self.assertEqual(total_speaks['oo'], result.oosp1 + result.oosp2)
        self.assertEqual(total_speaks['cg'], result.cgsp1 + result.cgsp2)
        self.assertEqual(total_speaks['co'], result.cosp1 + result.cosp2)

    def testCreateResultFromSpeaks(self):
        result = generate_objects.valid_result_with_debate()
        result.og,result.oo,result.cg,result.co = None,None,None,None
        result.add_positions_from_speaks()

        self.assertEqual(result.og, 0)
        self.assertEqual(result.oo, 1)
        self.assertEqual(result.cg, 2)
        self.assertEqual(result.co, 3)

    def testRaiseExceptionIfRoundHasPassed(self):
        result = generate_objects.valid_result_with_debate()
        tournament = Tournament.instance()
        tournament.round = 2
        tournament.save()
        with self.assertRaises(TournamentStateException):
            result.full_clean()