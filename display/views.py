from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import View

from display.controllers.TeamStandingController import TeamStandingController
from draw.models import Debate, Tournament
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

        team_standing_controller = TeamStandingController()
        results_controller = ResultsController()
        max_round = results_controller.max_round_with_results()

        template = loader.get_template('display/team_standing.html')
        context = RequestContext(request, {
            'table' : team_standing_controller.team_standing_table_all_rounds(),
            'max_round' : max_round,
            'all_rounds' : range(1, max_round+1)
        })
        return HttpResponse(template.render(context))
