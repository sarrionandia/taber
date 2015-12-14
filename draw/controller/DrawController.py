from draw.models import Tournament, TournamentStateException, Debate


class DrawController():

    def create_pools(self):

        from results.controllers import ResultsController
        if not ResultsController.results_entered_for_round(Tournament.instance().round):
            raise TournamentStateException("All results for current round must be entered to draw")

        return []

