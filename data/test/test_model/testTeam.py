from data.models import Institution, Team
from django.test import TestCase

from data.test import generate_objects


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

    def testGetDebate(self):
        debate = generate_objects.valid_debate()
        debate.save()
        debate2 = generate_objects.valid_debate()
        debate2.save()

        self.assertEqual(debate, debate.OG.debate_for_round(1))
        self.assertEqual(debate, debate.OO.debate_for_round(1))
        self.assertEqual(debate, debate.CG.debate_for_round(1))
        self.assertEqual(debate, debate.CO.debate_for_round(1))
