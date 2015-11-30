from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.template import RequestContext, loader
from models import Institution, Judge, Team
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    template = loader.get_template('data/index.html')
    context = RequestContext(request, {
        'institutions' : Institution.objects.all().order_by('name'),
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


class CreateInstitutionView(View):
    def post(self, request):
        name = request.POST.get('name')
        institution = Institution(name=name)
        institution.save()

        response = {"id" : institution.id,
                    "name" : institution.name}
        return HttpResponse(json.dumps(response))

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CreateInstitutionView, self).dispatch(*args, **kwargs)


class UpdateInstitutionView(View):

    def post(self, request, institutionid):
        try:
            institution = Institution.objects.get(id=institutionid)
            institution.name = request.POST.get('name')
            institution.save()

            response = {
                'name' : institution.name,
                'id' : institution.id
            }

            return HttpResponse(json.dumps(response));

        except ObjectDoesNotExist:
            raise Http404("Institution does not exist")

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UpdateInstitutionView, self).dispatch(*args, **kwargs)

class DeleteTeamView(View):
    def post(self, request, teamid):
        try:
            team = Team.objects.get(id=teamid)
            team.delete()
        except ObjectDoesNotExist:
            raise Http404("Team does not exist")
        return HttpResponse("OK")

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DeleteTeamView, self).dispatch(*args, **kwargs)
