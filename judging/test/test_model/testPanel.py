from django.test import TestCase

from data.test import generate_objects
from draw.models import TournamentStateException
from judging.models import Panel


class PanelTestCase(TestCase):

    def testAllowsValidPanel(self):
        judges = [generate_objects.valid_judge(), generate_objects.valid_judge(), generate_objects.valid_judge()]
        chair = judges[1]
        debate = generate_objects.valid_debate()
        debate.save()

        panel = Panel(chair=chair)
        panel.debate = debate
        panel.save()

        panel.judges.add(judges[0], judges[1], judges[2])

        panel.full_clean()
        panel.save()

    def testChairNotInPanel(self):
        judges = [generate_objects.valid_judge(), generate_objects.valid_judge(), generate_objects.valid_judge()]
        chair = generate_objects.valid_judge()
        debate = generate_objects.valid_debate()
        debate.save()

        panel = Panel(chair=chair)
        panel.debate = debate
        panel.save()
        panel.judges.add(judges[0], judges[1], judges[2])
        with self.assertRaises(TournamentStateException):
            panel.full_clean()