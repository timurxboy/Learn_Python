class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles
      
def sweetest_icecream(lst):
    table = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5, 'Strawberry': 10, 'Chocolate': 10}

    maxx = 0
    for i in lst:
        a = table[i.flavor] + i.sprinkles
        if maxx < a:
            maxx = a
    return maxx



ice1 = IceCream("Chocolate", 13)         # 10 + 13 = 23
ice2 = IceCream("Vanilla", 0)           # 5 + 0 = 5
ice3 = IceCream("Strawberry", 7)         # 10 + 7 = 17
ice4 = IceCream("Plain", 18)             # 0 + 18 = 18
ice5 = IceCream("ChocolateChip", 3)      # 5 + 3 = 8
sweetest_icecream([ice1, ice2, ice3, ice4, ice5])
sweetest_icecream([ice3, ice1])
sweetest_icecream([ice3, ice5])