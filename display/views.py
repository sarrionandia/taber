from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import View

from data.models import Team
from draw.models import Debate, Tournament
from results.controllers.PointsController import PointsController
from results.controllers.ResultsController import ResultsController


class DrawTableView(View):

    def get(self, request, round):
        template = loader.get_template('display/table.html')
        context = RequestContext(request, {
            'display_round' : int(round),
            'debates' : Debate.objects.all().filter(round=round),
            'max_round' : Tournament.instance().round,
            'all_rounds' : range(1, Tournament.instance().round+1)
        })
        return HttpResponse(template.render(context))

class TeamStandingView(View):
    def get(self, request):
        rows = []

        round = Tournament.instance().round
        results_controller = ResultsController()
        points_controller = PointsController()
        if not results_controller.results_entered_for_round(round):
            round -= 1

        teams = list(Team.objects.all())
        teams.sort(key= lambda team: team.total_team_points, reverse=True)
        for t in range(0, len(teams)):
            team = teams[t]
            row = [t+1, team]
            for r in range(1,round+1):
                row.append(points_controller.team_points_for_team(team, r))
                row.append(team.total_team_points)
            rows.append(row)
        template = loader.get_template('display/team_standing.html')
        context = RequestContext(request, {
            'table' : rows,
            'max_round' : round,
            'all_rounds' : range(1, round+1)
        })
        return HttpResponse(template.render(context))
