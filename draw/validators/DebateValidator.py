from django.core.exceptions import ValidationError

def validate(debate, all_debates):
    validate_team_unique(debate, all_debates)

def validate_team_unique(unique_debate, all_debates_in_round):
    if (len(unique_debate.positions().values()) > (len(set(unique_debate.positions().values())))):
        raise ValidationError("A team can't be in two positions in one room")

    for debate in all_debates_in_round:
        if any(x in debate.positions().values() for x in unique_debate.positions().values()):
            raise ValidationError("A team can't be in two debates in the same round")
