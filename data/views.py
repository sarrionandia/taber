from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Institution, Judge, Team
def index(request):


    template = loader.get_template('data/index.html')
    context = RequestContext(request, {
        'institutions' : Institution.objects.all(),
        'judges' : Judge.objects.all(),
        'teams' : Team.objects.all()
    })

    return HttpResponse(template.render(context))