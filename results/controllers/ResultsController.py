from draw.controller.DebateController import DebateController
from draw.models import TournamentStateException, Tournament, Debate


class ResultsController():

    debate_controller = DebateController()

    def results_entered_for_round(self, round):
        if round > Tournament.instance().round:
            raise TournamentStateException("Round has not yet been drawn")

        for debate in Debate.objects.filter(round=round):
            if not debate.has_result:
                return False
        return True

    def result_for_team(self, team, round):
        debate = self.debate_controller.debate_for_round(team, round)
        return debate.result

    def max_round_with_results(self):
        current_round = Tournament.instance().round
        if self.results_entered_for_round(current_round):
            return current_round
        else:
            return current_round - 1