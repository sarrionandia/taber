from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from django.views.generic import View

from data.models import Team
from draw.models import Debate, Tournament
from forms import ResultForm
from results.controllers.PointsController import PointsController


class EditResultsView(View):

    def get(self, request, debateid):
        debate = Debate.objects.get(id=debateid)
        template = loader.get_template('results/edit_result.html')
        form = ResultForm(initial={'debate': debateid})
        context = RequestContext(request, {
            'form' : form,
            'debate' : debate
        })
        return HttpResponse(template.render(context))

    def post(self, request, debateid):
        form = ResultForm(request.POST)

        if form.is_valid():
            result = Debate.objects.get(id=debateid).result
            print form.cleaned_data
            result.ogsp1 = form.cleaned_data['ogsp1']
            result.ogsp2 = form.cleaned_data['ogsp2']
            result.oosp1 = form.cleaned_data['oosp1']
            result.oosp2 = form.cleaned_data['oosp1']
            result.cgsp1 = form.cleaned_data['cgsp1']
            result.cgsp2 = form.cleaned_data['cgsp2']
            result.cosp1 = form.cleaned_data['cosp1']
            result.cosp2 = form.cleaned_data['cosp2']

            result.add_positions_from_speaks()

        else:
            return HttpResponseBadRequest()

        result.full_clean()
        result.save()
        return HttpResponse(result.id)


class CurrentResultsTableView(View):
    def get(self, request):
        return HttpResponseRedirect('/results/round/' + str(Tournament.instance().round))

class ResultsTableView(View):
    def get(self, request, round):

        if int(round) < 1 or int(round) > Tournament.instance().round:
            raise Http404

        points_controller = PointsController()

        debates = Debate.objects.filter(round=round)
        template = loader.get_template('results/results_table.html')
        context = RequestContext(request, {
            'round' : int(round),
            'debates' : debates,
            'max_round' : Tournament.instance().round,
            'all_rounds' : range(1, Tournament.instance().round+1),
            'points' : points_controller.team_points_map_for_round(Tournament.instance().round, Team.objects.all())

        })
        return HttpResponse(template.render(context))

        return HttpResponse(round)