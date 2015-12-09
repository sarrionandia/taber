from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.template import loader, RequestContext
from django.views.generic import View

from draw.models import Debate, Tournament
from forms import ResultForm
from results.models import Result


class EditResultsView(View):

    def get(self, request, debateid):
        debate = Debate.objects.get(id=debateid)
        template = loader.get_template('results/edit_result.html')
        form = ResultForm(initial={'debate': debateid})
        context = RequestContext(request, {
            'form' : form,
            'debate' : debate,
        })
        return HttpResponse(template.render(context))

    def post(self, request, debateid):
        form = ResultForm(request.POST)

        if form.is_valid():
            result = Result(debate=Debate.objects.get(id=debateid))
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

class ResultsTableView(View):
    def get(self, request, round):

        if int(round) < 1 or int(round) > Tournament.instance().round:
            print("ROUND>> ", Tournament.instance().round)
            raise Http404

        debates = Debate.objects.filter(round=round)
        template = loader.get_template('results/results_table.html')
        context = RequestContext(request, {
            'round' : round,
            'debates' : debates,
        })
        return HttpResponse(template.render(context))

        return HttpResponse(round)