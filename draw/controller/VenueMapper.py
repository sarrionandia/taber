from data.models import Venue
from draw.models import Debate, TournamentStateException


class VenueMapper():

    def map_venues(self, round):

        debates = list(Debate.objects.all().filter(round=round))
        venues = list(Venue.objects.all())

        if len(venues) < len(debates):
            raise TournamentStateException("There are not enough venues to allocate for this round")

        for i in range(0, len(debates)):
            debates[i].venue = venues[i]
            debates[i].save()
            