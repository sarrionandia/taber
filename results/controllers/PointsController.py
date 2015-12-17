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

    def total_points_for_team(self, team, maxround):
        total = 0
        for round in range(1, maxround+1):
            total += self.team_points_for_team(team, round)
        return total

    def speaker_points_for_team(self, team, round):
        result = self.results_controller.result_for_team(team, round)
        debate = result.debate

        if debate.OG == team:
            return [result.ogsp1, result.ogsp2]
        if debate.OO == team:
            return [result.oosp1, result.oosp2]
        if debate.CG == team:
            return [result.cgsp1, result.cgsp2]
        if debate.CO == team:
            return [result.cosp1, result.cosp2]
