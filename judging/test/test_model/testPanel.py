from django.test import TestCase

from data.test import generate_objects
from draw.models import TournamentStateException
from judging.models import Panel


class PanelTestCase(TestCase):

    def setUp(self):
        panel = Panel()
        debate = generate_objects.valid_debate()
        debate.save()
        panel.debate = debate
        judges = [generate_objects.valid_judge(), generate_objects.valid_judge(), generate_objects.valid_judge()]
        panel.chair = judges[1]
        panel.save()
        panel.judges.add(judges[0], judges[1], judges[2])
        panel.save()
        self.panel = panel

    def testAllowsValidPanel(self):
        self.panel.full_clean()
        self.panel.save()

    def testChairNotInPanel(self):
        panel = self.panel
        panel.chair = generate_objects.valid_judge()
        with self.assertRaises(TournamentStateException):
            panel.full_clean()

    def testJudgeInTwoPanelsForSameRound(self):
        duplicate_judge = self.panel.judges.all().first()
        panel = Panel()
        debate = generate_objects.valid_debate()
        debate.save()
        panel.debate = debate
        panel.chair = duplicate_judge
        panel.save()
        panel.judges.add(duplicate_judge)
        with self.assertRaises(TournamentStateException):
            panel.full_clean()