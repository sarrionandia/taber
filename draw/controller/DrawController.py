from draw.models import Tournament, TournamentStateException
from results.controllers.ResultsController import ResultsController


class DrawController():

    resultsController = ResultsController()

    def create_pools(self):
        if not self.resultsController.results_entered_for_round(Tournament.instance().round):
            raise TournamentStateException("All results for current round must be entered to draw")

        return []

