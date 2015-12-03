from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import View
from forms import ResultForm


class EditResultsView(View):

    def get(self, request, debateid):
        template = loader.get_template('results/edit_result.html')
        form = ResultForm()
        context = RequestContext(request, {
            'form' : form,
        })
        return HttpResponse(template.render(context))

