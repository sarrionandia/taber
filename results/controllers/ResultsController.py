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

def team_points_for_team(team, round):
    result = result_for_team(team, round)
    debate = result.debate

    if debate.OG == team:
        return result.og
    if debate.OO == team:
        return result.oo
    if debate.CG == team:
        return result.cg
    if debate.CO == team:
        return result.co