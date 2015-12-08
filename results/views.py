from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import View

from draw.models import Debate
from forms import ResultForm


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


class PreviewResultsView(View):

    def post(self, request, debateid):

        return HttpResponse("OK")



