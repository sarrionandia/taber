from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import View

from display.controllers.TeamStandingController import TeamStandingController
from draw.models import Debate, Tournament


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

        round = Tournament.instance().round
        team_standing_controller = TeamStandingController()

        template = loader.get_template('display/team_standing.html')
        context = RequestContext(request, {
            'table' : team_standing_controller.team_standing_table_all_rounds(),
            'max_round' : round,
            'all_rounds' : range(1, round+1)
        })
        return HttpResponse(template.render(context))
