print(issubclass.__doc__)
help(issubclass)

class Shape:
    pass
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

circle = Circle(10)

print(issubclass(Circle, Shape))

print(isinstance(circle, Circle))
print(isinstance(circle, Shape))

print(isinstance(1, int))
print(isinstance('1', str))
print(isinstance(23.2, float))
print(isinstance(1, str))

print(callable(circle)) # objects than defines __call__() is considered callable
print(callable(print))

if hasattr(circle, 'radius'):
    print(getattr(circle, 'radius'))
    setattr(circle, 'radius', 20)
    print(getattr(circle, 'radius'))

print(dir(circle))
print(circle.__dict__)

print(Circle.__name__)
print(__name__)

print(type(circle))

circle2 = circle
print(id(circle))
print(id(circle2))


print(repr(circle))