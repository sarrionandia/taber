from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Institution

def index(request):


    template = loader.get_template('data/index.html')
    context = RequestContext(request, {
        'institutions' : Institution.objects.all()
    })

    return HttpResponse(template.render(context))