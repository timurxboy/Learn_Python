from enum import IntFlag
class Color(IntFlag):
    RED = 1
    GREEN = 2 
    BLUE = 4

combination = Color.GREEN | Color.RED

print(combination)

print(Color.RED in combination)