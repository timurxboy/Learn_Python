from enum import IntEnum
class Priority(IntEnum):
    LOW = 1
    NORMAL = 2
    HING = 3

print(Priority.LOW<Priority.HING)