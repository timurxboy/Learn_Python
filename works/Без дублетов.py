def calc_dice_scores(lst):
    # ваше решение
    return sum([a+b for a,b in lst]) if not any(a==b for a,b in lst) else 0
