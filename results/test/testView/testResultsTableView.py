from django.http import Http404
from django.test import TestCase

from draw.models import Tournament
from results.views import ResultsTableView


class ResultsTableTestCase(TestCase):
    
    def testThrows404ForRound0(self):
        view = ResultsTableView()
        with self.assertRaises(Http404):
            view.get(None, 0)

    def testThrows404ForTooHighRound(self):
        tournament = Tournament.instance()
        tournament.save()
        view = ResultsTableView()
        with self.assertRaises(Http404):
            view.get(None, 2)
