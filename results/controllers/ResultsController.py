from draw.models import TournamentStateException, Tournament, Debate


def results_entered_for_round(round):
    if round > Tournament.instance().round:
        raise TournamentStateException("Not all results are input for this round")

    for debate in Debate.objects.filter(round=round):
        if not debate.has_result:
            return False
    return True