from enum import Enum
class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    EARTH = (5.976e+24, 6.37814e6)
    JUPITER = (1.9e+27, 7.1492e7)

    def __init__(self, maass, radius):
        self.mass = maass
        self.radius = radius

    @property
    def surface_gravity(self):
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)


print(Planet.EARTH.value)
print(Planet.EARTH.surface_gravity)
