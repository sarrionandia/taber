from tab.models import *


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
    debate.chair = valid_judge()
    debate.venue = valid_venue()
    debate.round = 1
    return debate
