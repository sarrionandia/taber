from django.http import Http404
from django.test import TestCase
from data.test import generate_objects
from data.views import DeleteTeamView
from data.models import Team


class TeamTestCase(TestCase):
    def testDeleteTeam(self):
        team_id = generate_objects.valid_team().id
        view = DeleteTeamView()
        view.post(None, team_id)

        self.assertEqual(0, Team.objects.filter(id=team_id).count(), "Didn't delete team")
