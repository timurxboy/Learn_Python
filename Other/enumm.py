from enum import Enum
class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
print(TrafficLight.RED)
print(TrafficLight.RED.name)
print(TrafficLight.RED.value)


