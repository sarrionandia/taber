from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.template import RequestContext, loader
from models import Institution, Judge, Team
from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('data/index.html')
    context = RequestContext(request, {
        'institutions' : Institution.objects.all(),
        'judges' : Judge.objects.all(),
        'teams' : Team.objects.all()
    })
    return HttpResponse(template.render(context))

class DeleteInstitutionView(View):

    def post(self, request, institutionid):


        try:
            institution = Institution.objects.get(id=institutionid)
            institution.delete()
        except ObjectDoesNotExist:
            raise Http404("Institution does not exist")

        return HttpResponse(institutionid)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DeleteInstitutionView, self).dispatch(*args, **kwargs)
