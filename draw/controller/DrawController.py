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
        pools = self.create_blank_pools(max_round)

        for team in teams:
            points = self.pointsController.total_points_for_team(None, 1)
            pools[points].append(team)

        return pools

    @staticmethod
    def create_blank_pools(max_round):
        pools = {}
        if max_round == 0:
            return pools

        for points in range(0, 4 + ((max_round-1) * 3)):
            pools.update({points:[]})
        return pools

    @staticmethod
    def remove_empty(pools):
        keys = pools.keys()
        for key in keys:
            pool = pools[key]
            if len(pool) < 1:
                pools.pop(key)
        return pools

    @staticmethod
    def balance_pools(pools):
        if len([item for sublist in pools.values() for item in sublist]) % 4 != 0:
            raise ValueError("Number of teams must be divisible by 4")
        return None

