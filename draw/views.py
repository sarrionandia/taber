from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.views.generic import View

from data.models import Team, Venue
from draw.controller.InitialDrawController import InitialDrawController
from draw.controller.VenueMapper import VenueMapper
from draw.models import Tournament
from results.controllers.ResultsController import ResultsController


class DrawControl(View):
    def get(self, request):
        template = loader.get_template('draw/index.html')

        team_count = Team.objects.all().count()
        results_controller = ResultsController()
        tournament = Tournament.instance()

        context = RequestContext(request, {
            'teams_count' : Team.objects.all().count(),
            'teams_ok' : (team_count % 4 == 0) and (team_count >= 4),
            'rooms' : team_count / 4,
            'venues_ok' : Venue.objects.all().count() >= team_count/4,
            'tournament' : tournament,
            'this_round' : tournament.round,
            'next_round' : tournament.round + 1,
            'results_entered' : results_controller.results_entered_for_round(tournament.round)
        })
        return HttpResponse(template.render(context))

class DrawFirstRound(View):
    def post(self, request):
        controller = InitialDrawController()
        controller.initial_draw()
        mapper = VenueMapper()
        mapper.map_venues(1)
        return redirect('/draw')