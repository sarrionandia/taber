from data.models import Team, Judge
from draw.models import Debate


class InitialDrawController():

    def initial_draw(self):

        teams = Team.objects.all().order_by('?')
        num_debates = teams.count() / 4
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

        return debates