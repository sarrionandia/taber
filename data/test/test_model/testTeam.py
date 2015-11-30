from data.models import Institution, Team, Speaker
from django.test import TestCase


class TeamTestCase(TestCase):

    def setUp(self):
        Institution.objects.create(name='University of Whoville')
        self.team = Team.objects.create(name="A", institution = Institution.objects.get(name='University of Whoville'))
        Speaker(name="Eliot", team=self.team).save()
        Speaker(name='George', team=self.team).save()

    def test_return_string(self):
        expected = 'University of Whoville A'
        actual = Team.objects.get(name='A').__str__()
        self.assertEqual(expected, actual)

    def test_get_speakers(self):
        self.assertEqual(2, self.team.speakers.count())