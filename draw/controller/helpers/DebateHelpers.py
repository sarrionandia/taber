def debate_as_strings(debate):
    from results.controllers.PointsController import PointsController
    points_controller = PointsController()
    strings = []
    teams = [debate.OG, debate.OO, debate.CG, debate.CO]
    for team in teams:
        string = str(team)
        result= points_controller.team_points_for_team(team, debate.round)
        if result != None:
            result = str(result)
        strings.append([string, result])
    return strings
