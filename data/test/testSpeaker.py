from django.core.exceptions import ValidationError

from data.models import Institution, Team, Speaker
from django.test import TestCase


class SpeakerTestCase(TestCase):

    def setUp(self):
        Institution.objects.create(name='University')
        Team.objects.create(name='A', institution=Institution.objects.get(name='University'))
        Speaker.objects.create(name="Tito", team = Team.objects.get(name='A'))

    def test_return_string(self):
        expected = 'Tito <University A>'
        actual = Speaker.objects.get(name='Tito').__str__()
        self.assertEqual(expected, actual)

    def test_only_two_speakers_per_team(self):
        team = Team.objects.get(name='A')
        PM = Speaker(name="PM", team=team)
        DPM = Speaker(name="DPM", team=team)
        PM.save()
        DPM.save()

        with self.assertRaises(ValidationError):
            WTF = Speaker(name="WTF", team=team)
            WTF.full_clean()