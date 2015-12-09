from draw.models import Tournament, TournamentStateException
from results.controllers import ResultsController


class DrawController():

    def create_pools(self):

        if not ResultsController.results_entered_for_round(Tournament.instance().round):
            raise TournamentStateException("All results for current round must be entered to draw")



        return []

