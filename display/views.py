from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import View

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
