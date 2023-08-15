from collections import Counter

def is_full_house(a: list):
    a_dict = Counter(a)
    if len(a_dict)==2:
        if 2 in a_dict.values():
            return True
    return False

print(is_full_house(["A", "A", "A", "K", "K"]))
print(is_full_house(["3", "J", "J", "3", "3"]))
print(is_full_house(["10", "J", "10", "10", "10"]))
print(is_full_house(["7", "J", "3", "4", "2"]))