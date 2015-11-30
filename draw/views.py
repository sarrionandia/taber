from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.generic import View

class DrawControl(View):
    def get(self, request):
        template = loader.get_template('draw/index.html')
        context = RequestContext(request, {

        })
        return HttpResponse(template.render(context))