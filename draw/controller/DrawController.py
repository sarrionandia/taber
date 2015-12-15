from draw.models import Tournament, TournamentStateException
from results.controllers.PointsController import PointsController
from results.controllers.ResultsController import ResultsController


class DrawController():

    resultsController = None
    pointsController = None

    def __init__(self):
        self.resultsController = ResultsController()
        self.pointsController = PointsController()

    def create_pools(self, teams, max_round):
        if not self.resultsController.results_entered_for_round(Tournament.instance().round):
            raise TournamentStateException("All results for current round must be entered to draw")

        return []

    def create_blank_pools(self, max_round):
        pools = {}
        if max_round == 0:
            return pools

        for points in range(0, max_round*4):
            pools.update({points:[]})
        return pools