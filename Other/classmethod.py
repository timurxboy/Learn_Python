class MyClass():
    y = 2
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    @classmethod
    def from_string(cls, string):
        a , b = map(int,string.split(','))
        return cls(a,b,cls.y)
    
x = MyClass.from_string('1,2')
print(x.a, x.b)