from draw.models import Debate


class PanelController():

    def panels_for_round(self, round):
        debates = Debate.objects.filter(round=round)
        panels = []
        for debate in debates:
            panels.append(debate.panel_set.all().first())
        return panels

    def panels_for_judge(self, judge, round):
        panels = judge.panel_set
        result = []
        for panel in panels:
            if panel.debate.round == round:
                result.append(panel)
        return result