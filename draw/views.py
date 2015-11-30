from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.views.generic import View

from data.models import Team
from draw.controller.InitialDrawController import InitialDrawController


class DrawControl(View):
    def get(self, request):
        template = loader.get_template('draw/index.html')

        team_count = Team.objects.all().count()

        context = RequestContext(request, {
            'teams_count' : Team.objects.all().count(),
            'teams_ok' : (team_count % 4 == 0) and (team_count >= 4),
            'rooms' : team_count / 4,
        })
        return HttpResponse(template.render(context))

class DrawFirstRound(View):
    def post(self, request):
        controller = InitialDrawController()
        controller.initial_draw()
        return redirect('/draw')