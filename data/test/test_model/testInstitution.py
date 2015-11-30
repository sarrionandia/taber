from data.models import Institution, Team
from django.test import TestCase


class InstitutionTestCase(TestCase):

    def setUp(self):
        self.institution = Institution.objects.create(name='University of Whoville')

    def test_return_string(self):
        expected = 'University of Whoville'
        actual = Institution.objects.get(name='University of Whoville').__str__()
        self.assertEqual(expected, actual)


    def test_teams_query(self):
        team1 = Team(name="A", institution=self.institution)
        team2 = Team(name="B", institution=self.institution)
        team1.save()
        team2.save()

        self.assertEqual(self.institution.teams.count(), 2, "Didn't return all teams")