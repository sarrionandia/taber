from data.models import Team
from draw.models import Debate, TournamentStateException, Tournament


class InitialDrawController():

    def initial_draw(self):

        tournament = Tournament.instance()
        if tournament.round != 0:
            raise TournamentStateException("Round must be 0 for initial draw to happen")

        teams = Team.objects.all().order_by('?')
        num_teams = teams.count()

        if num_teams < 4:
            raise TournamentStateException("Number of teams must be 4 or more")

        if num_teams%4 != 0:
            raise TournamentStateException("Number of teams must be a multiple of 4")

        num_debates = num_teams / 4
        debates = []

        for i in range(0,num_debates):
            debate = Debate()
            debate.round = 1
            debate.OG = teams[(i*4) +0]
            debate.OO = teams[(i*4) +1]
            debate.CG = teams[(i*4) +2]
            debate.CO = teams[(i*4) +3]

            debate.save()
            debates.append(debate)

        tournament.round = 1
        tournament.save()

        return debates