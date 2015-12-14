from django.core.exceptions import ValidationError

def validate(result):
    check_positions_awarded(result)
    check_position_matches_speaks(result)


def check_positions_awarded(result):
        results = [result.og, result.oo, result.cg, result.co]
        if not 0 in results:
            raise ValidationError("4th was not awarded")
        if not 1 in results:
            raise ValidationError("3rd was not awarded")
        if not 2 in results:
            raise ValidationError("2nd was not awarded")
        if not 3 in results:
            raise ValidationError("1st was not awarded")


def check_position_matches_speaks(result):
        speaks = result.total_speaks()
        speaks_order = sorted(speaks, key=speaks.get)
        if result.positions()[speaks_order[0]] != 0:
            raise ValidationError("Team in 4th must have lowest speaker score")
        if result.positions()[speaks_order[1]] != 1:
            raise ValidationError("Team in 3rd must have second lowest speaker score")
        if result.positions()[speaks_order[2]] != 2:
            raise ValidationError("Team in 2nd must have second highest speaker score")
        if result.positions()[speaks_order[3]] != 3:
            raise ValidationError("Team in 1st must have highest speaker score")
