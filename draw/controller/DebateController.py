from draw.models import Debate


class DebateController():

    def debate_for_round(self, team, round):
        debates = Debate.objects.filter(round=round)
        if debates.filter(OG=team).count() > 0:
            return debates.filter(OG=team).first()
        if debates.filter(OO=team).count() > 0:
            return debates.filter(OO=team).first()
        if debates.filter(CG=team).count() > 0:
            return debates.filter(CG=team).first()
        if debates.filter(CO=team).count() > 0:
            return debates.filter(CO=team).first()
        return None
