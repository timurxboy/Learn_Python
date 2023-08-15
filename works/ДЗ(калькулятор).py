class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a*b
    
    def divide(self, a, b):
        return a/b

n = Calculator()
print(n.add(10,5))
print(n.subtract(10,5))
print(n.divide(10,5))
print(n.multiply(10,5))
