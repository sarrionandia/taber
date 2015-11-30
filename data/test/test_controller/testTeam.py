import json

from django.http import Http404
from django.test import TestCase, RequestFactory

from data.models import Team, Speaker
from data.test import generate_objects
from data.views import DeleteTeamView, CreateTeamView, UpdateTeamView


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

    def testCreateTeamJSONResponse(self):
        institution = generate_objects.valid_institution()
        view = CreateTeamView()
        request = self.factory.post('/data/team/create/',
                                    data={
                                        'name' : 'TeamName',
                                        'speaker1' : 'Alice',
                                        'speaker2' : 'Jennie',
                                        'institution' : institution.id
                                    })
        response = json.loads(view.post(request).content)

        self.assertIsNotNone(response['name'], "No team name returned by create team function")
        self.assertIsNotNone(response['id'], "No team ID returned by create team function")
        self.assertIsNotNone(response['speaker1'], "No speaker1 returned by create team function")
        self.assertIsNotNone(response['name'], "No speaker2 returned by create team function")

    def testTeamCreatesDatabaseObjects(self):
        institution = generate_objects.valid_institution()
        view = CreateTeamView()
        request = self.factory.post('/data/team/create/',
                                    data={
                                        'name' : 'TeamName',
                                        'speaker1' : 'Alice',
                                        'speaker2' : 'Jennie',
                                        'institution' : institution.id
                                    })
        response = json.loads(view.post(request).content)

        team = Team.objects.get(id=response['id'])

        self.assertEqual(response['name'], team.name, "Team name didn't match created team")

        for speaker in team.speakers:
            self.assertTrue(speaker.name == response['speaker1'] or speaker.name == response['speaker2'],
                            "Speaker name didn't match created speaker")


    def testUpdateTeamChangesDatabaseObject(self):
        team = generate_objects.valid_team()
        sp1 = Speaker(name='oldsp1', team=team)
        sp2 = Speaker(name='oldsp2', team=team)
        sp1.save()
        sp2.save()

        request = self.factory.post('/data/team/' + str(team.id) + '/update/',
                                    data={
                                        'name': 'New Name',
                                        'speaker1' : 'newsp1',
                                        'speaker2' : 'newsp2',
                                        'institution' : team.institution.id
                                    })
        view = UpdateTeamView()
        view.post(request, team.id)

        team.refresh_from_db()

        self.assertEqual("New Name", team.name, "Team name wasn't updated")
        for speaker in team.speakers:
            self.assertTrue(speaker.name == 'newsp1' or speaker.name == 'newsp2', "Speaker name wasn't updated: " + speaker.name)


    def testUpdateTeamWithTeamDoesntExist(self):
        view = UpdateTeamView()

        with self.assertRaises(Http404):
            view.post(None, 0)