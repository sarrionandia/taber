from data.models import Team
from draw.models import Tournament
from results.controllers.PointsController import PointsController
from results.controllers.ResultsController import ResultsController


class TeamStandingController():

    points_controller = None
    results_controller = None

    def __init__(self):
        self.points_controller = PointsController()
        self.results_controller = ResultsController()

    def team_standing_table_all_rounds(self):
        round = Tournament.instance().round
        if not self.results_controller.results_entered_for_round(round):
            round -= 1
        return self.team_standing_table(round)

    def team_standing_table(self, max_round):
            rows = []
            teams = list(Team.objects.all())
            teams.sort(key= lambda team: (team.total_team_points, team.total_speaker_sum), reverse=True)
            for t in range(0, len(teams)):
                team = teams[t]
                if (team.total_speaker_sum == teams[t-1].total_speaker_sum) and (team.total_team_points == teams[t-1].total_team_points):
                    row = ['--', team]
                else:
                    row = [t+1, team]
                for r in range(1,max_round+1):
                    row.append(self.points_controller.team_points_for_team(team, r))
                row.append(team.total_speaker_sum)
                row.append(team.total_team_points)
                rows.append(row)
            return rows
