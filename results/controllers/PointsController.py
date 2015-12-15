from results.controllers.ResultsController import ResultsController


class PointsController():

    results_controller = None

    def __init__(self):
        self.results_controller = ResultsController()

    def team_points_for_team(self, team, round):
        result = self.results_controller.result_for_team(team, round)
        debate = result.debate

        if debate.OG == team:
            return result.og
        if debate.OO == team:
            return result.oo
        if debate.CG == team:
            return result.cg
        if debate.CO == team:
            return result.co