from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

Color.BLUE
print(Color.RED)
print(Color.GREEN)
print(Color.BLUE)

print(list(Color))