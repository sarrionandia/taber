from draw.models import TournamentStateException, Tournament, Debate


def results_entered_for_round(round):
    if round > Tournament.instance().round:
        raise TournamentStateException("Round has not yet been drawn")

    for debate in Debate.objects.filter(round=round):
        if not debate.has_result:
            return False
    return True

def result_for_team(team, round):
    debate = team.debate_for_round(round)
    return debate.result