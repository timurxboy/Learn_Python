from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        print('Base DRAW')

    @abstractmethod
    def area(self):
        print('Base AREA')

    @abstractmethod
    def perimetr(self):
        print('Base PERIMETR')

    @abstractmethod
    def drag(self):
        print('Base DRAG')



class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print('No Base DRAW')

    def area(self):
        print('No Base AREA')

    def perimetr(self):
        print('No Base PERIMETR')
        return self.a+self.b+self.c

    def drag(self):
        print('No Base DRAG')
    
    

t = Triangle(10,10,10)
print(t.perimetr())