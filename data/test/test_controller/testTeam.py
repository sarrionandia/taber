from django.http import Http404
from django.test import TestCase, RequestFactory

from data.models import Team
from data.test import generate_objects
from data.views import DeleteTeamView, CreateTeamView


class TeamTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()


    def testDeleteTeam(self):
        team_id = generate_objects.valid_team().id
        view = DeleteTeamView()
        view.post(None, team_id)

        self.assertEqual(0, Team.objects.filter(id=team_id).count(), "Didn't delete team")

    def testDeleteTeamDoesntExist(self):
        view = DeleteTeamView()
        with self.assertRaises(Http404):
            view.post(None, 0)

    def testCreateTeam(self):
        institution = generate_objects.valid_institution()
        teams_count = Team.objects.all().count()
        view = CreateTeamView()
        request = self.factory.post('/data/team/create/',
                                    data={
                                        'name' : 'TeamName',
                                        'speaker1' : 'Alice',
                                        'speaker2' : 'Jennie',
                                        'institution' : institution.id
                                    })
        view.post(request)

        self.assertEqual(teams_count+1, Team.objects.all().count(), "Didn't create a new team")
