from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import View

from draw.models import Debate


class DrawTableView(View):

    def get(self, request, round):
        template = loader.get_template('display/table.html')
        context = RequestContext(request, {
            'round' : round,
            'debates' : Debate.objects.all().filter(round=round)
        })
        return HttpResponse(template.render(context))
