from data.models import Venue
from draw.models import Debate, TournamentStateException


class VenueMapper():

    def map_venues(self, round):

        if Venue.objects.all().count() < Debate.objects.all().filter(round=round):
            raise TournamentStateException("There are not enough venues to allocate for this round")

        return True