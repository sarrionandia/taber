from django.http import Http404
from django.test import TestCase

from results.views import ResultsTableView


class ResultsTableTestCase(TestCase):

    def testThrows404ForRound0(self):
        view = ResultsTableView()
        with self.assertRaises(Http404):
            view.get(None, 0)