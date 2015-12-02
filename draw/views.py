from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.views.generic import View

from data.models import Team, Venue
from draw.controller.InitialDrawController import InitialDrawController
from draw.controller.VenueMapper import VenueMapper
from draw.models import Tournament


class DrawControl(View):
    def get(self, request):
        template = loader.get_template('draw/index.html')

        team_count = Team.objects.all().count()

        context = RequestContext(request, {
            'teams_count' : Team.objects.all().count(),
            'teams_ok' : (team_count % 4 == 0) and (team_count >= 4),
            'rooms' : team_count / 4,
            'venues_ok' : Venue.objects.all().count() >= team_count/4,
            'tournament' : Tournament.instance()
        })
        return HttpResponse(template.render(context))

class DrawFirstRound(View):
    def post(self, request):
        controller = InitialDrawController()
        controller.initial_draw()
        mapper = VenueMapper()
        mapper.map_venues(1)
        return redirect('/draw')