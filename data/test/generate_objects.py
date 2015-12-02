from data.models import *
from draw.models import *
from results.models import Result


def valid_team():
    team = Team(name="Team")
    team.institution = valid_institution()
    team.save()
    return team


def valid_institution():
    institution =  Institution(name="University")
    institution.save()
    return institution


def valid_judge():
    judge = Judge(name="Judge")
    judge.institution = valid_institution()
    judge.save()
    return judge


def valid_venue():
    venue = Venue(name="room")
    venue.save()
    return venue

def valid_debate():
    debate = Debate()
    debate.OG = valid_team()
    debate.CG = valid_team()
    debate.OO = valid_team()
    debate.CO = valid_team()
    debate.round = 1
    return debate

def valid_result_with_debate():
    debate = valid_debate()
    debate.save()
    result = Result(debate=debate)
    result.og = 0
    result.oo = 1
    result.cg = 2
    result.co = 3

    result.ogsp1 = 65
    result.ogsp2 = 66
    result.oosp1 = 67
    result.oosp2 = 68
    result.cgsp1 = 69
    result.cgsp2 = 70
    result.cosp1 = 71
    result.cosp2 = 72

    result.save()
    return result