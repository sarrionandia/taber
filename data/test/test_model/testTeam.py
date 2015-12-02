from data.models import Institution, Team
from django.test import TestCase


class TeamTestCase(TestCase):

    def setUp(self):
        Institution.objects.create(name='University of Whoville')
        self.team = Team.objects.create(name="A",
                                        institution = Institution.objects.get(name='University of Whoville'))
        self.team.speaker1 = 'Eliot'
        self.team.speaker2 = 'George'

    def test_return_string(self):
        expected = 'University of Whoville A'
        actual = Team.objects.get(name='A').__str__()
        self.assertEqual(expected, actual)
